import requests
from requests_folder.delete_meal_plan_day import *
from requests_folder.connect_user import connect_user
import datetime


class TestDeleteMealPlanDay:
    def test_delete_meal_plan_day(self):
        r = connect_user()
        r_username = r['username']
        r_user_hash = r['hash']
        date = datetime.date.today()
        response = delete_meal_plan_day(r_username, date, r_user_hash)
        assert response.status_code == 200, f'ERROR! Expected status code is 200, actual status code is {r.status_code}'
        assert response.json()["status"] == "success"




