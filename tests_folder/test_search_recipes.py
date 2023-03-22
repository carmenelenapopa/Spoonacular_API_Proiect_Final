from requests_folder.search_recipes import search_recipes

class TestSearchRecipes:
    def test_search_recipes(self):
        r = search_recipes()
        assert r.status_code == 200, f"ERROR! Expected status code 200, actual {r.status_code}"
        assert len(r.json()) == 4, f"Expected: 4, actual: {len(r.json())}"
        assert r.json()['totalResults'] == 5221







        


