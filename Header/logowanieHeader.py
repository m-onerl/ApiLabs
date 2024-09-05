import requests
import json   
from pprint import pprint
from credentials import headers

r = requests.get('https://api.thecatapi.com/v1/favourites/', headers = headers)



try:
    content = r.json()
except json.decoder.JSONDecodeError:
    print("Bad format") 
else:
    print(content)


    