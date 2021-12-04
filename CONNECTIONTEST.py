#CONNECTIONTEST
#Filip Rokita
#www.filiprokita.com

import requests

url=input("URL: ")

try:
    request = requests.get(url, timeout=5)
    print("Connection")
except:
    print("Connection Error")