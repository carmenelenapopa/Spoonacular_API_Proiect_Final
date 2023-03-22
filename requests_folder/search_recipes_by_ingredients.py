import requests
import json

def search_recipes_by_ingredients(ingredients, number, ignorePantry):
    api_url_base = f'https://api.spoonacular.com/recipes/findByIngredients?ingredients={ingredients}&number={number}&ignorePantry={ignorePantry}'
    headers = {'Content-Type': 'application/json'}
    params = {'apiKey': '9c9d5c3d17b44aa2bddf934fc45912cc'}
    r = requests.get(api_url_base, headers=headers, params=params)
    return r



