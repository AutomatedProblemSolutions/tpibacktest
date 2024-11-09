import requests


def get_data_1(sheet_name, print_data):
    url = f'https://script.google.com/macros/s/AKfycbz5mJEV8UeCT4Jn8NAZnj_Poq5OCXQ--E8XNcMK306g8ZDdyFf73p0fMo9YximVmIGK/exec?sheet={sheet_name}'
    response = requests.get(url)
    data = response.json()
    return data[print_data]


def get_data_2(sheet_name, print_data):
    url = f'https://script.google.com/macros/s/AKfycbwYJCJRtOgJZVfzFdDUYKBTZ31BLrIbsB2WgoD5AYrVFTlLIbRz5bLh4cOQJz7ue8og/exec?sheet={sheet_name}'
    response = requests.get(url)
    data = response.json()
    return data[print_data]


def get_data_3(sheet_name, print_data):
    url = f'https://script.google.com/macros/s/AKfycbyaA_HAya6Q8yo-jccGKLE1IFCFWnhxFJpxg8Tglq_27ryXc2vRbdbNZ33piL0aaUba/exec?sheet={sheet_name}'
    response = requests.get(url)
    data = response.json()
    return data[print_data]


def get_data_4(sheet_name, print_data):
    url = f'https://script.google.com/macros/s/AKfycbzFoNYspLkMEstlLuBXene_6HwAvp3koFG-EPBa5tPfY2GtCAntrgHAHGgMZWsgEu99/exec?sheet={sheet_name}'
    response = requests.get(url)
    data = response.json()
    return data[print_data]


def get_data_5(sheet_name, print_data):
    url = f'https://script.google.com/macros/s/AKfycbzeV7EnwWC2zVn44XBPncVmzG57reavqu4lln--icQX_vK3dWSu8t7m39KrYu_oOyVA/exec?sheet={sheet_name}'
    response = requests.get(url)
    data = response.json()
    return data[print_data]

