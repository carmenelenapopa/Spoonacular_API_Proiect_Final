import requests
import json


def compute_glycemic_load_banana():
    api_url_base = 'https://api.spoonacular.com/food/ingredients/glycemicLoad'
    headers = {
        "Content-Type": "application/json",
        "x-api-key": "9c9d5c3d17b44aa2bddf934fc45912cc"
    }

    response_headers = {"Content-Type: application/json"}

    request_body = {
        "ingredients": [
            "1 banana",
            "1 apple",
            "2 glasses of milk"

        ]
    }

    r = requests.post(api_url_base, headers=headers, json=request_body)
    return r
