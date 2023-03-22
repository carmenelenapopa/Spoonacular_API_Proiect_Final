from requests_folder.search_ingredients import search_ingredients

class TestSearchInformations:
    def test_search_ingredients(self):
        r = search_ingredients('apple', 'egg', 10, 'true')
        assert r.status_code == 200, f'ERROR! Expected status code is 200, actual status code is {r.status_code}'
        assert r.json()["totalResults"] == 39
        assert r.json()['results'][0]["id"] == 9003
        assert r.json()['results'][0]["name"] == "apple"
        assert r.json()['results'][1]["name"] == "applesauce"

    def test_search_ingredients1(self):
        r = search_ingredients('avocado', 'gluten', 10, 'true')
        assert r.status_code == 200, f'ERROR! Expected status code is 200, actual status code is {r.status_code}'
        assert r.json()["totalResults"] == 7
        assert r.json()['results'][0]["id"] == 9037
        assert r.json()['results'][0]["name"] == "avocado"
        assert r.json()['results'][1]["name"] == "avocado oil"

    def test_search_ingredients2(self):
        r = search_ingredients('milk', 'nuts', 10, 'false')
        assert r.status_code == 200, f'ERROR! Expected status code is 200, actual status code is {r.status_code}'
        assert r.json()["totalResults"] == 54
        assert r.json()['results'][0]["id"] == 1077
        assert r.json()['results'][0]["name"] == "milk"
        assert r.json()['results'][1]["name"] == "milky way"

    def test_search_ingredients3(self):
        r = search_ingredients('patrunjel', 'gluten', 10, 'false')
        assert r.status_code == 200, f'ERROR! Expected status code is 200, actual status code is {r.status_code}'
        assert r.json()["totalResults"] == 0
