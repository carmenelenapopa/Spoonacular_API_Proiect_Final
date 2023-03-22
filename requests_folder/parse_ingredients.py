
import requests
import json

def parse_ingredients(ingredientList, servings, includeNutrition):
    api_url_base = "https://api.spoonacular.com/recipes/parseIngredients"
    headers = {
        "Content-Type": "application/x-www-form-urlencoded",
        "x-api-key": "9c9d5c3d17b44aa2bddf934fc45912cc"
    }
    params = {
        "ingredientList": ingredientList,
        "servings": servings,
        "includeNutrition": includeNutrition,
        "language": "en",
    }
    response = requests.post(api_url_base, headers=headers, data=params)
    return response



