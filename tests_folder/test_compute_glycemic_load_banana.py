from requests_folder.compute_glycemic_load_kiwi import *
import requests

from requests_folder.compute_glycemic_load_banana import compute_glycemic_load_banana


class TestComputeGlycemicLoad:
    def test_compute_glycemic_load_banana_apple_milk(self):
        r = compute_glycemic_load_banana()
        assert r.status_code == 200, f'ERROR! Expected status code 200, actual {r.status_code}'
        assert r.json()['status'] == 'success'
        assert r.json()['totalGlycemicLoad'] == 28.08
        assert len(r.json()["ingredients"]) == 3


