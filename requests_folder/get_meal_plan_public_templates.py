import requests
import json

def get_meal_plan_public_templates():
    api_url_base = "https://api.spoonacular.com/mealplanner/public-templates"
    headers = {
            "Content-Type": "application/json",
            "x-api-key": "9c9d5c3d17b44aa2bddf934fc45912cc"
    }
    r = requests.get(api_url_base, headers=headers)
    return r

