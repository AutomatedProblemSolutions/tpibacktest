import streamlit as st
import api
import pandas as pd
import numpy as np
import plotly.graph_objects as go


# Layout
st.set_page_config(layout = "wide")


# Title of the dashboard
st.title('Backtesting Tool')


# Input for the sheet name
sheet_name = "R1"


# Input for the specific data (daily returns) to use in backtesting
backtest_for = st.text_input("Enter the key for daily returns (e.g., 'daily_returns'):")


# File upload widget (only accepts CSV files)
uploaded_file = st.file_uploader("Upload a CSV file", type="csv")


@st.cache_data(ttl=600)
def calculate_equities(daily_returns, tpi_data):
    """Calculate strategy and buy-and-hold equities based on daily returns and TPI signals."""
    strategy_equity = [1]  # Starting equity for strategy
    buy_and_hold_equity = [1]  # Starting equity for buy-and-hold


    # Calculate the equity based on signals in 'tpi' column
    for i, signal in enumerate(tpi_data):
        if i < len(daily_returns):
            daily_return = daily_returns[i]


            # Strategy equity update based on 'tpi' signal
            if signal > 0:
                strategy_equity.append(strategy_equity[-1] * (1 + daily_return))  # Long
            elif signal < 0:
                strategy_equity.append(strategy_equity[-1] * (1 - daily_return))  # Short
            else:
                strategy_equity.append(strategy_equity[-1])  # Neutral/cash


            # Buy-and-hold equity (always long)
            buy_and_hold_equity.append(buy_and_hold_equity[-1] * (1 + daily_return))
        else:
            # If daily returns data is shorter than tpi data
            strategy_equity.append(strategy_equity[-1])
            buy_and_hold_equity.append(buy_and_hold_equity[-1])


    return strategy_equity, buy_and_hold_equity


# Button to perform backtest if conditions are met
if st.button("Perform Backtest"):
    if sheet_name and backtest_for and uploaded_file is not None:
        try:
            # Fetch data using the get_data_1 function from api.py
            daily_returns_data = api.get_data_1(sheet_name, backtest_for)
            daily_returns = pd.Series(daily_returns_data)  # Convert to Pandas Series


            # Read the uploaded CSV file
            df = pd.read_csv(uploaded_file)


            # Ensure 'tpi' and 'date' columns exist in the uploaded CSV file
            if 'tpi' in df.columns and 'date' in df.columns:


                # Calculate and cache the equities
                strategy_equity, buy_and_hold_equity = calculate_equities(daily_returns, df['tpi'])


                # Function to plot the equity chart
                def plot_equity_chart(yaxis_type='linear', title_suffix=''):
                    fig = go.Figure()
                    fig.add_trace(go.Scatter(x=df['date'], y=strategy_equity[1:], mode='lines', name='Strategy Equity'))
                    fig.add_trace(go.Scatter(x=df['date'], y=buy_and_hold_equity[1:], mode='lines', name='Buy and Hold Equity'))
                   
                    # Customize layout with adjustable y-axis type
                    fig.update_layout(
                        title=f"Strategy Equity vs. Buy and Hold Over Time {title_suffix}",
                        xaxis_title="Date",
                        yaxis_title="Equity",
                        legend_title="Equity Curves",
                        yaxis_type=yaxis_type  # Set the y-axis to either linear or log scale
                    )
                    return fig


                # Display both charts side by side
                col1, col2 = st.columns(2)
                with col1:
                    st.plotly_chart(plot_equity_chart(yaxis_type='linear', title_suffix="(Linear Scale)"))
                with col2:
                    st.plotly_chart(plot_equity_chart(yaxis_type='log', title_suffix="(Log Scale)"))


            else:
                st.error("The uploaded CSV file must contain both 'tpi' and 'date' columns.")
        except Exception as e:
            st.error(f"Error fetching data or processing backtest: {e}")
    else:
        st.warning("Please enter the sheet name, key for daily returns, and upload a CSV file.")

