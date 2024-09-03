import requests
import json   
import sys
import credentials


from pprint import pprint

r = requests.get('https://api.thecatapi.com/v1/favourites/', headers = headers)


try:
    content = r.json()
except json.decoder.JSONDecodeError:
    print("Bad format") 
else:
    print(content)