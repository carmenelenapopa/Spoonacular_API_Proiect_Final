import requests
import json

def add_meal_plan_template(username, user_hash ):
    api_url_base = f"https://api.spoonacular.com/mealplanner/{username}/templates?hash={user_hash}"
    headers = {
            "Content-Type": "application/json",
            "x-api-key": "9c9d5c3d17b44aa2bddf934fc45912cc"
    }

    # "x-api-key": "9c9d5c3d17b44aa2bddf934fc45912cc"
    request_body = {
    "name": "My new meal plan template",
    "items": [
        {
            "day": 1,
            "slot": 1,
            "position": 0,
            "type": "RECIPE",
            "value": {
                "id": 296213,
                "servings": 2,
                "title": "Spinach Salad with Roasted Vegetables and Spiced Chickpea",
                "imageType": "jpg"
            }
        },
        {
            "day": 2,
            "slot": 1,
            "position": 0,
            "type": "PRODUCT",
            "value": {
                "id": 183433,
                "servings": 1,
                "title": "Ahold Lasagna with Meat Sauce",
                "imageType": "jpg"
            }
        },
        {
            "day": 3,
            "slot": 1,
            "position": 0,
            "type": "MENU_ITEM",
            "value": {
                "id": 378557,
                "servings": 1,
                "title": "Pizza 73 BBQ Steak Pizza, 9",
                "imageType": "png"
            }
        },
        {
            "day": 4,
            "slot": 1,
            "position": 0,
            "type": "CUSTOM_FOOD",
            "value": {
                "id": 348,
                "servings": 1,
                "title": "Aldi Spicy Cashews - 30g",
                "image": "https://spoonacular.com/cdn/ingredients_100x100/cashews.jpg"
            }
        },
        {
            "day": 5,
            "slot": 1,
            "position": 0,
            "type": "INGREDIENTS",
            "value": {
                "ingredients": [
                    {
                        "name": "1 banana"
                    },
                    {
                        "name": "coffee",
                        "unit": "cup",
                        "amount": "1",
                        "image": "https://spoonacular.com/cdn/ingredients_100x100/brewed-coffee.jpg"
                    }
                ]
            }
        }
    ],
    "publishAsPublic": False
}
    r = requests.post(api_url_base, headers=headers, json=request_body)
    return r




