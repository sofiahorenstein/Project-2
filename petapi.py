import requests
import json


API_KEY = "n82rLvtiyqelro1uziEkHOjNpk1Iq9MF3r0OfSBDA6bQltSExj"
SECRET = "0jr9tbtWMj362Oe3ha92r4tyLe5W05bmNoKYUjrI"


def _get_bearer_token():
    response=requests.post("https://api.petfinder.com/v2/oauth2/token", data={
        'grant_type': 'client_credentials',
        'client_id': API_KEY,
        'client_secret': SECRET})
    return response.json()["access_token"]


def get_url(url):
    bearer_token = _get_bearer_token()
    return requests.get(url, headers={"Authorization": f"Bearer {bearer_token}"})


def get_pets(num_pages):
    pets = []
    for i in range(1, num_pages): 
        response = get_url(f"https://api.petfinder.com/v2/animals?page={i}")
        x = json.loads(response.text)
        pets.extend(x["animals"])

    return pets

