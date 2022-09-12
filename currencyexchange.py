from errno import EUSERS
import requests
import pprint
import os
import sys

def get_codes(): # this gets the list of country code symbols that are available from this API
    url = 'https://api.exchangerate.host/symbols'
    response = requests.get(url)
    data = response.json()
    return data
      
def check_code(country_codes,code_to_check): # check that the user input exists in the list of country codes
    if code_to_check in country_codes['symbols']:
        return True
    else:
        return False

def do_conversion(first_code,second_code): # Take the two country codes and pass them to the convert API
    params = {'from': first_code, 'to': second_code}
    url = 'https://api.exchangerate.host/convert'

    response = requests.get(url, params=params)
    data = response.json()
    data.pop('motd')
    conversion_rate = (data['result'])
    print("The conversion rate from %s to %s is %s" % (first_code.upper(),second_code.upper(),"{:.2f}".format(conversion_rate)))
    # print("The conversion rate from %s to %s is %s" % (first_code.upper(),second_code.upper(),conversion_rate))
    # print("{:.2f}".format(conversion_rate))

if __name__ == "__main__":
    os.system('cls')
    country_codes = get_codes()
    print('This script will take two country codes as input and display the currency conversion rate. \n')

    while(True):
        first_code = input('\nPlease enter the first 3-letter country code. Type (l) for a (l)ist of codes (Warning: long). (q) to (q)uit:\n')
        if (first_code == 'l'):
            country_codes.pop('motd') 
            country_codes.pop('success')
            pprint.pprint(country_codes)
            continue
        elif (first_code == 'q'):
            print('Exiting')
            sys.exit(0)
        else:
            if check_code(country_codes,first_code.upper()):
                pass
            else:
                print('That country code was not found')
                continue
        while(True):
            second_code = input('\nEnter the second 3-letter country code:\n')
            if check_code(country_codes,second_code.upper()):
                do_conversion(first_code,second_code)
                break
            else:
                print('The second country code was NOT found')
                user_continue = input("\nWould you like to try again? (y/n)?\n")
                if(user_continue.lower() == 'y'):
                    continue
                else:
                    sys.exit(0)