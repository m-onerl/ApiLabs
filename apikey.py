import requests
import json

params = {
    "api_key": "vqWBAPZe0wVToG97IcdcfEIHamZ1zwBI",  
    "country": "pl",
    "year": 2024,
    "month": 12
}

r = requests.get("https://calendarific.com/api/v2/holidays", params=params)

try:
    content = r.json()
except json.decoder.JSONDecodeError: 
    print("Bad format")
else:
    for holiday in content['response']['holidays']:
        print(f"Name of Holiday: {holiday['name']}")
        print(f"Description of Holiday: {holiday['description']}")
        print(f"Date of Holiday: {holiday['date']['iso']}")
        print(f"Type of Holiday: {', '.join(holiday['type'])}")
        print()  
