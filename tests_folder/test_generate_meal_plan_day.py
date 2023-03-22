from requests_folder.generate_meal_plan_day import *
import requests

class TestGenerateMealPlanDay:
    def test_generate_meal_plan_day1(self):
        r = generate_meal_plan_day('day', 2000, 'vegetarian', 'shellfish, olives')
        assert r.status_code == 200, f'ERROR! Expected status code is 200, actual status code is {r.status_code}'

    def test_generate_meal_plan_day2(self):
        r = generate_meal_plan_day('day', 2500, 'vegetarian', 'gluten')
        assert r.status_code == 200, f'ERROR! Expected status code is 200, actual status code is {r.status_code}'

    def test_generate_meal_plan_day3(self):
        r = generate_meal_plan_day('day', 1800, 'pescetarian', 'dairies')
        assert r.status_code == 200, f'ERROR! Expected status code is 200, actual status code is {r.status_code}'