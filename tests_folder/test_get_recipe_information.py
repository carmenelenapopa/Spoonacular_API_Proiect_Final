import requests

from requests_folder.get_recipe_information import recipe_information_byID

class TestSearchRecipesById:
    # testing get recipes information by a valid ID - 716429
    def test_get_recipes_informations_by_id(self):
        r = recipe_information_byID('716429', 'false')
        assert r.status_code == 200, f'ERROR! Expected status code is 200, actual status code is {r.status_code}'
        assert r.json()["vegetarian"] == False
        assert r.json()["pricePerServing"] == 157.06
        assert r.json()["title"] == "Pasta with Garlic, Scallions, Cauliflower & Breadcrumbs"

    # testing get recipes information by a valid ID - 782585
    def test_get_recipes_informations_by_id1(self):
        r = recipe_information_byID('782585', 'true')
        assert r.status_code == 200, f'ERROR! Expected status code is 200, actual status code is {r.status_code}'
        assert r.json()["vegetarian"] == True
        assert r.json()["pricePerServing"] == 134.63

    # negativ testing - get recipes information by invalid ID
    def test_search_recipes_by_invalid_id(self):
        r = recipe_information_byID('500102456789', 'true')
        assert r.status_code == 404, f'ERROR! Expected status code is 404, actual status code is {r.status_code}'
