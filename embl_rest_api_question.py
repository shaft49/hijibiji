#!/bin/python3

import sys
import os
import requests
import urllib
import urllib.request
import json


# Complete the function below.
# https://jsonmock.hackerrank.com/api/countries/search?name=
def  getCountries(s, p):
    page = 1
    num_of_countries = 0
    while True:
        url = f'https://jsonmock.hackerrank.com/api/countries/search?name={s}&page={page}'
        response = requests.get(url)
        json_data = response.json()
        total = len(json_data['data'])
        if total == 0:
            break
        for data in json_data['data']:
            if data['population'] > p:
                num_of_countries += 1
        page += 1
    print(num_of_countries)
    return num_of_countries
# f = open(os.environ['OUTPUT_PATH'], 'w')
    
getCountries('un', 100090)
# try:
#     _s = str(input())
# except:
#     _s = None


# _p = int(input());

# res = getCountries(_s, _p)
# f.write(str(res) + "\n")

# f.close()
