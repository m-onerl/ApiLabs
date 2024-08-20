import requests
import json

params = {
    "amount" : 5,
    "animal_type" : "",
}
choose = input("""Choose what kind of home animal friend facts you want to see:
1. Cats
2. Dogs \n""")
    
if choose == "1":
        params["animal_type"] = "cat"
elif choose == "2":
        params["animal_type"] = "dog"
else:
     print("Invalid choice")
     exit()
     
r = requests.get("https://cat-fact.herokuapp.com/facts/random", params)

try:
    getattr = r.json()
except json.decoder.JSONDecodeError:
    print("Bad format")
else:
    for fact in getattr:
        print(fact["text"])
