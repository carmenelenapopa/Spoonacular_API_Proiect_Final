import requests
import json

def compute_glycemic_load_kiwi():

    api_url_base = 'https://api.spoonacular.com/food/ingredients/glycemicLoad'
    headers = {
            "Content-Type": "application/json",
            "x-api-key": "9c9d5c3d17b44aa2bddf934fc45912cc"
    }

    response_headers = {"Content-Type: application/json"}

    param = {
    "ingredients": [
        "1 kiwi",
        "2 cups rice",
        "2 glasses of water"
    ]
}
    r = requests.post(api_url_base, headers=headers, json=param)
    return r




