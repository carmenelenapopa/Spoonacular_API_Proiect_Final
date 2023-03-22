import requests
import json

from requests_folder.parse_ingredients import parse_ingredients


class TestParseIngredients:
    def test_parse_ingredients_greentea(self):
        r = parse_ingredients('1 cup green tea', '1', 'true')
        assert r.status_code == 200, f'ERROR! Expected status code is 200, actual status code is {r.status_code}'
        assert r.json()[0]["id"] == 10014355
        assert r.json()[0]["originalName"] == "green tea"


    def test_parse_ingredients_carrot(self):
        r = parse_ingredients('carrot', '1', 'true')
        assert r.status_code == 200, f'ERROR! Expected status code is 200, actual status code is {r.status_code}'
        assert r.json()[0]["id"] == 11124
        assert r.json()[0]["originalName"] == "carrot"

    def test_parse_ingredients_patrunjel(self):
        r = parse_ingredients('patrunjel', '1', 'true')
        assert r.status_code == 200, f'ERROR! Expected status code is 200, actual status code is {r.status_code}'
        assert r.json()[0]["meta"] == []
        assert r.json()[0]["originalName"] == "patrunjel"

