import requests
import json

r = requests.get("")

try:
    questions = r.json
except json.decoder.JSONDecodeError:
    print("Niepoprawny format")
else:
    print("Nothing")