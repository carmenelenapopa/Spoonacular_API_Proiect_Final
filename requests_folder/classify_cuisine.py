import requests
import json

def classify_cuisine(title, ingredientList):
    api_url_base = f'https://api.spoonacular.com/recipes/cuisine?title={title}&ingredientList={ingredientList}'
    headers = {'Content-Type': 'application/x-www-form-urlencoded'}
    params = {'apiKey': '9c9d5c3d17b44aa2bddf934fc45912cc'}
    r = requests.post(api_url_base, headers=headers, params=params)
    return r



