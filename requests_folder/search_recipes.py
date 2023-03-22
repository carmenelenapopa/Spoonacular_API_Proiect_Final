import requests
import json

def search_recipes():
    api_url_base = 'https://api.spoonacular.com/recipes/complexSearch'
    headers = {'Content-Type': 'application/json'}
    params = {'apiKey': '9c9d5c3d17b44aa2bddf934fc45912cc'}
    r = requests.get(api_url_base, headers=headers, params=params)
    return r






