from requests_folder.add_meal_plan_template import add_meal_plan_template
import requests
import json

from requests_folder.connect_user import connect_user


class TestAddMealPlanTemplate:
    def test_add_meal_plan_template(self):
        r = connect_user()
        r_username = r['username']
        r_user_hash = r['hash']
        r = add_meal_plan_template(r_username, r_user_hash)
        assert r.status_code == 200, f'ERROR! Expected status code 200, actual {r.status_code}'


