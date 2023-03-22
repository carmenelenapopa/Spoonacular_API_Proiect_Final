import requests
import json


def connect_user():
    url = "https://api.spoonacular.com/users/connect"
    headers = {
        "Content-Type": "application/json",
        "x-api-key": "9c9d5c3d17b44aa2bddf934fc45912cc"
    }
    data = {
        "username": "carmen_giol@yahoo.com",
        "firstName": "Carmen",
        "lastName": "Popa",
        "email": "carmen_giol@yahoo.com"
    }
    params = {"apiKey": "9c9d5c3d17b44aa2bddf934fc45912cc"}
    response = requests.post(url, headers=headers, params=params, data=json.dumps(data))
    if response.status_code == 200:
        user_data = response.json()  # Store user data in global variable

        return user_data

    else:
        return "Error connecting user: " + response.text

