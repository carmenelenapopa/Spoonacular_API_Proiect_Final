import requests
import json

def get_ingredient_information(id, amount, unit):
    api_url_base = f'https://api.spoonacular.com/food/ingredients/{id}/information?amount={amount}&unit={unit}'
    headers = {'Content-Type': 'application/json'}
    params = {'apiKey': '9c9d5c3d17b44aa2bddf934fc45912cc'}
    r = requests.get(api_url_base, headers=headers, params=params)
    return r



