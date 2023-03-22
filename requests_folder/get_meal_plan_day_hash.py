import requests
import json

def get_meal_plan_day_hash(username, date, hash):
    api_url_base = f'https://api.spoonacular.com/mealplanner/?usename={username}&date={date}&hash={hash}'
    headers = {
        "Content-Type": "application/json",
        "x-api-key": "9c9d5c3d17b44aa2bddf934fc45912cc"
    }
    response_headers = {'Content-Type': 'application/json'}
    r = requests.get(api_url_base, headers=headers)
    return r

