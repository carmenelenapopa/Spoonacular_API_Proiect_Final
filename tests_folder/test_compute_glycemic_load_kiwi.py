from requests_folder.compute_glycemic_load_kiwi import *
import requests
import json

class TestComputeGlycemicLoad:
    def test_compute_glycemic_load_kiwi_rice_water(self):
        r = compute_glycemic_load_kiwi()
        assert r.status_code == 200, f'ERROR! Expected status code 200, actual {r.status_code}'
        assert r.json()['status'] == 'success'
        assert r.json()['totalGlycemicLoad'] == 183.32
        assert len(r.json()["ingredients"]) == 3

