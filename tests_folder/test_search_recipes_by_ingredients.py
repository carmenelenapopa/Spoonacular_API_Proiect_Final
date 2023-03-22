import requests
from requests_folder.search_recipes_by_ingredients import search_recipes_by_ingredients


class TestSearchRecipesByIngredients:
    # testing search recipes by specific ingredient - avocado
    def test_search_recipes_by_ingredients_avocado(self):
        r = search_recipes_by_ingredients('avocado', '10', 'true')
        assert r.status_code == 200, f'ERROR! Expected status code is 200, actual status code is {r.status_code}'

    # testing search recipes by specific ingredient - apple
    def test_search_recipes_by_ingredients_apple(self):
        r = search_recipes_by_ingredients('apple', '3', 'true')
        assert r.status_code == 200, f'ERROR! Expected status code is 200, actual status code is {r.status_code}'

    # testing search recipes by specific ingredient - tuna
    def test_search_recipes_by_ingredients_tuna(self):
        r = search_recipes_by_ingredients('tuna', '5', 'false')
        assert r.status_code == 200, f'ERROR! Expected status code is 200, actual status code is {r.status_code}'

    # testing search recipes by an invalid ingredient - mamaliga
    def test_search_recipes_by_ingredients_mamaliga(self):
        r = search_recipes_by_ingredients('mamaliga', '5', 'false')
        assert r.status_code == 200, f'ERROR! Expected status code is 200, actual status code is {r.status_code}'
        assert len(r.json()) == 0

