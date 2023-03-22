from requests_folder.get_ingredient_information import get_ingredient_information
import requests
import json

class TestGetIngredientInformation:
    def test_get_ingredient_information(self):
        r = get_ingredient_information(9266, 150, 'grams')
        assert r.status_code == 200, f'ERROR! Expected status code is 200, actual status code is {r.status_code}'
        assert r.json()['originalName'] == "pineapples"
        assert r.json()['categoryPath'][0] == "tropical fruit"

    def test_get_ingredient_information1(self):
        r = get_ingredient_information(9003, 100, 'grams')
        assert r.status_code == 200, f'ERROR! Expected status code is 200, actual status code is {r.status_code}'
        assert r.json()['originalName'] == "apples"
        assert r.json()['categoryPath'][0] == "fruit"

    def test_get_ingredient_information2(self):
        r = get_ingredient_information(1077, 100, 'mililiters')
        assert r.status_code == 200, f'ERROR! Expected status code is 200, actual status code is {r.status_code}'
        assert r.json()['originalName'] == "dairy milk"
        assert r.json()['categoryPath'][0] == "drink"
