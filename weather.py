from datetime import datetime
import os
import pytz
import requests
import math
API_KEY = '93180ba8527181831afe7c0a86b2a8e7'
API_URL = ('http://api.openweathermap.org/data/2.5/weather?id={}&mode=json&units=metric&appid={}')

def query_api(cid):
    try:
        #print(API_URL.format(cid, API_KEY))
        data = requests.get(API_URL.format(cid, API_KEY)).json()
    except Exception as exc:
        print(exc)
        data = None
    return data
