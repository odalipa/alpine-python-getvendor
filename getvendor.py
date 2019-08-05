import requests
import sys

# API URL
url = "https://api.macaddress.io/v1"
# API Key
apiKey = "at_nNvyTDHLOB91TF61rW7wLcDvLhq2z"
# Desired output format
output = "json"

# if command line argument is not provoded
if len(sys.argv) == 1:
    # ask user for MAC
    macaddr = input("Enter MAC address: ")
else:
    # else take first argument as MAC
    macaddr = sys.argv[1]

# Form the complete API Query
# Example:
# https://api.macaddress.io/v1?apiKey=at_nNvyTDHLOB91TF61rW7wLcDvLhq2z&output=json&search=c8:d9:d2:a9:f5:7f
query = url + "?" + "apiKey=" + apiKey + "&" + "output=" + output + "&" + "search=" + macaddr

# Try to make a API request
try:
    # Place request
    result = requests.get(query)
    # Collect data - data is returned as a python dictionary
    data = result.json()
    # If data has error in its key then print error
    if 'error' in data:
        print(data['error'])
    # Else print relevant keys from data
    else:
        print("API Query:", query)
        print("MAC Address:", macaddr)
        print("OUI:", data['vendorDetails']['oui'])
        print("Comapny Name:", data['vendorDetails']['companyName'])
        print("Company Address:", data['vendorDetails']['companyAddress'])
        print("Company Country Code:", data['vendorDetails']['countryCode'])
# If try fails print error message to User
except:
    print('Requested API is not reachable: check your network connection and api query')
