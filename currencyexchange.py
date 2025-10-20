import requests
import pprint
import os
import sys

# === CHANGED: Now uses Frankfurter API (no API key needed) ===
def get_codes():
    url = 'https://api.frankfurter.app/currencies'
    response = requests.get(url)
    data = response.json()
    return {'symbols': data}  # match original structure for compatibility

def check_code(country_codes, code_to_check):
    symbols = country_codes.get('symbols', {})
    return code_to_check.upper() in symbols

# === CHANGED: Now uses Frankfurter API endpoint for conversion ===
def do_conversion(first_code, second_code):
    url = 'https://api.frankfurter.app/latest'
    params = {'from': first_code.upper(), 'to': second_code.upper()}
    response = requests.get(url, params=params)
    data = response.json()
    rate = data.get('rates', {}).get(second_code.upper())

    if rate:
        print(f"The conversion rate from {first_code.upper()} to {second_code.upper()} is {rate}")
    else:
        print("Conversion not available for those currencies.")

if __name__ == "__main__":
    os.system('cls' if os.name == 'nt' else 'clear')
    country_codes = get_codes()
    print('This script will take two country codes as input and display the currency conversion rate.\n')

    while True:
        first_code = input('\nPlease enter the first 3-letter country code. Type (l) for a (l)ist of codes (Warning: long). (q) to (q)uit:\n')

        if first_code.lower() == 'l':
            pprint.pprint(country_codes['symbols'])
            continue
        elif first_code.lower() == 'q':
            print('Exiting')
            sys.exit(0)
        else:
            if not check_code(country_codes, first_code):
                print('That country code was not found')
                continue
                
        second_code = input('\nEnter the second 3-letter country code:\n')
        if check_code(country_codes, second_code):
            do_conversion(first_code, second_code)
            break
        else:
            print('The second country code was NOT found')
            user_continue = input("\nWould you like to try again? (y/n)? ")
            if user_continue.lower() == 'y':
                continue
            else:
                sys.exit(0)
