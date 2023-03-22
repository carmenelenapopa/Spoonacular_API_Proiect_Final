import requests
import json

def recipe_information_byID(id, includeNutrition):
    api_url_base = f'https://api.spoonacular.com/recipes/{id}/information?includeNutrition={includeNutrition}'
    headers = {'Content-Type': 'application/json'}
    params = {'apiKey': '9c9d5c3d17b44aa2bddf934fc45912cc'}
    r = requests.get(api_url_base, headers=headers, params=params)
    return r



