import requests
import json   
from pprint import pprint
import credentials 

def get_json_content_from_response(response):
    try:
        content = response.json()
    except json.decoder.JSONDecodeError:
        print("Bad format") 
    else:
        return content
def get_fav_cats(userId):
    params = {
        "sub_id" : userId
    }
    r = requests.get('https://api.thecatapi.com/v1/favourites/', params, headers = credentials.headers)

    return get_json_content_from_response(r)

def get_random_cat():
    r = requests.get('https://api.thecatapi.com/v1/images/search', headers = credentials.headers)

    return get_json_content_from_response(r)



print("Hej, zaloguj sie - podaj login oraz hasło")

userId = "agh2m"
name = "Sebastian"

print("Witaj " + name + "!")
favCats = get_fav_cats(userId)
print("Twoje ulubione kotki to", favCats)
randomCat = get_random_cat()
print("Wylosowano kotka", randomCat)
 
    