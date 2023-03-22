
from requests_folder.generate_meal_plan_week import *
import requests

class TestGenerateMealPlanWeek:

    def test_generate_meal_plan_week1(self):
        r = generate_meal_plan_week('week', 2300, 'lacto-vegetarian', 'nuts, gluten')
        assert r.status_code == 200, f'ERROR! Expected status code is 200, actual status code is {r.status_code}'

    def test_generate_meal_plan_week2(self):
        r = generate_meal_plan_week('week', 2000, 'ketogenic', 'dairies')
        assert r.status_code == 200, f'ERROR! Expected status code is 200, actual status code is {r.status_code}'

    def test_generate_meal_plan_week3(self):
        r = generate_meal_plan_week('week', 2500, 'paleo', 'beans, lentils')
        assert r.status_code == 200, f'ERROR! Expected status code is 200, actual status code is {r.status_code}'

