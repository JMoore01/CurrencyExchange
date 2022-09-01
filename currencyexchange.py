import requests
import pprint
import os
import sys

#TO DO: Put this in a function 
url = 'https://api.exchangerate.host/symbols'
response = requests.get(url)
data = response.json()

def get_input():
    first_code = input('Please enter the first 3-letter country code. Type (l) for a (l)ist of codes (Warning: long). (q) to (q)uit:\n')
    if (first_code == 'l'):
        data.pop('motd') #For use with api.exchangerate.host
        data.pop('success')  #For use with api.exchangerate.host
        pprint.pprint(data)
        get_input()
    elif (first_code == 'q'):
        print('Exiting')
        sys.exit(0)
    else:
        if check_code(first_code.upper()):
            print('Country code found')
        else:
            print('First code was not found')
            #TO DO: What action next?

    second_code = input('\nEnter the second country code:\n')
    if check_code(second_code.upper()):
        print('Second country code found')
    else:
        print('Second code NOT found')
        #TO DO: What action next?

# TO DO call function to show conversion rate do_conversion()
    do_conversion(first_code,second_code)
        
def check_code(code_to_check): #check the user input to see if it exists in the response
    if code_to_check in data['symbols']:
        print('Key was found')
        return True
    else:
        print('Key was NOT found')
        return False

def do_conversion(first_code,second_code): 
    params = {'from': first_code, 'to': second_code}
    url = 'https://api.exchangerate.host/convert'

    response = requests.get(url, params=params)
    data = response.json()
    data.pop('motd')
    # print(response.url)
    # pprint.pprint(data)
    conversion_rate = (data['result'])
    print("The conversion rate from %s to %s is %s" % (first_code,second_code,conversion_rate))

if __name__ == "__main__":
    os.system('cls')
    print('This script will take two country codes as input and display the currency conversion rate. \n')
    get_input()