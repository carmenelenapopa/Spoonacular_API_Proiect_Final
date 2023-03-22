from requests_folder.get_meal_plan_public_templates import get_meal_plan_public_templates
import requests
import json

class TestGetMealPLanPublicTemplate:
    def test_get_meal_plan_public_templates(self):
        r = get_meal_plan_public_templates()
        assert r.status_code == 200, f'ERROR! Expected status code 200, actual {r.status_code}'
        # assert r.json()["templates"][0]["id"] == 128

