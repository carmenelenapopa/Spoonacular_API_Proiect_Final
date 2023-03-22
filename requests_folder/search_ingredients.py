import requests
import json

def search_ingredients(query, intolerances, number, metaInformation):
    api_url_base = f'https://api.spoonacular.com/food/ingredients/search?query={query}&intolerances={intolerances}&number={number}&metaInformation={metaInformation}'
    headers = {'Content-Type': 'application/json'}
    params = {'apiKey': '9c9d5c3d17b44aa2bddf934fc45912cc'}
    r = requests.get(api_url_base, headers=headers, params=params)
    return r



