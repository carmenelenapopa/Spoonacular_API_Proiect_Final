from requests_folder.connect_user import connect_user
from requests_folder.get_meal_plan_day_hash import get_meal_plan_day_hash
import requests

class TestGetMealPlanDayHash:
    def test_get_meal_plan_day_has(self):

        r = get_meal_plan_day_hash(connect_user()['username'], 2023 - 0o3 - 13, connect_user()['hash'])
        assert r.status_code == 200, f'ERROR! Expected status code is 200, actual status code is {r.status_code}'

