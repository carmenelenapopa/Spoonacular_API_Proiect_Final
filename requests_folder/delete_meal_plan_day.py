import requests


def delete_meal_plan_day(username, date, user_hash):
    api_url_base = f'https://api.spoonacular.com/mealplanner/{username}/day/{date}?hash={user_hash}'
    headers = {'Content-Type': 'application/json',
               'x-api-key': "9c9d5c3d17b44aa2bddf934fc45912cc"}
    r = requests.delete(api_url_base, headers=headers)
    return r






