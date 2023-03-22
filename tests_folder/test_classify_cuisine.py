from requests_folder.classify_cuisine import classify_cuisine
import requests
import json

class TestClassifyCuisine:
    def test_classify_cuisine1(self):
        r = classify_cuisine('Pork roast with green beans', '3 oz pork shoulder')
        assert r.status_code == 200, f'ERROR! Expected status code is 200, actual status code is {r.status_code}'
        assert r.json()["cuisine"] == "Mediterranean"


    def test_classify_cuisine2(self):
        r = classify_cuisine('Cauliflower, Brown Rice, and Vegetable Fried Rice', 'brown rice')
        assert r.status_code == 200, f'ERROR! Expected status code is 200, actual status code is {r.status_code}'
        assert r.json()["cuisine"] == "Chinese"

    def test_classify_cuisine3(self):
        r = classify_cuisine('Chicken Fajita Stuffed Bell Pepper', 'chicken meat')
        assert r.status_code == 200, f'ERROR! Expected status code is 200, actual status code is {r.status_code}'
        assert r.json()["cuisine"] == "Mexican"

    def test_classify_cuisine4(self):
        r = classify_cuisine('Branza cu mamliga si smantana', 'malai')
        assert r.status_code == 200, f'ERROR! Expected status code is 200, actual status code is {r.status_code}'
        assert r.json()["cuisine"] == "Mediterranean"

