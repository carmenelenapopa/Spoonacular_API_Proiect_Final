import requests
import json

def generate_meal_plan_day(timeFrame, targetCalories, diet, exclude):
    api_url_base = f'https://api.spoonacular.com/mealplanner/generate?timeFrame={timeFrame}&targetCalories={targetCalories}&diet={diet}&exclude={exclude}'
    headers = {
        "Content-Type": "application/json",
        "x-api-key": "9c9d5c3d17b44aa2bddf934fc45912cc"
    }

    r = requests.get(api_url_base, headers=headers)
    return r
