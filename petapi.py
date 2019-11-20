import requests
import json


API_KEY = "SVXPUGK0JZmTMpZxnIdoN1kn5enX1L4YI9O3zHjrkIGQ60SZc9"
SECRET = "bMGoUiUB5sa0pswsY4mpzsfBA9l8sZbL82DerzD0"


def _get_bearer_token():
    response=requests.post("https://api.petfinder.com/v2/oauth2/token", data={
        'grant_type': 'client_credentials',
        'client_id': API_KEY,
        'client_secret': SECRET})
    return response.json()["access_token"]


def get_url(url):
    bearer_token = _get_bearer_token()
    return requests.get(url, headers={"Authorization": f"Bearer {bearer_token}"})

response = get_url("https://api.petfinder.com/v2/animals?page=5")

x = json.loads(response.text)

print(json.dumps(x, indent = 4, sort_keys = True))

# print(get_url("https://api.petfinder.com/v2/types/{dog}/breeds").json)
