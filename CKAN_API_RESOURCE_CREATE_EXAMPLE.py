# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""


import requests

url = 'https://portal.addferti.eu/api/3/action/resource_create'
#filepath = 'N:/Daten_GG/projekte/2021_EU_BMBF_AddFerti_64130208/Data/CKAN_Data/Sample_Data/sample2.csv'
filepath = '/home/alex-laptop/Documents/Python/Sample_Data//sample.csv'
API_Key = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJqdGkiOiJaVkpCZ2hsSVh6TEVrZGxxTnBfNmoyQ0xnWlZJdUhZTVlkWTdhQmVsT0xkblNBMzBZNzl6ZFRDZEFtYW9TdGs1eElzT0dUTHF3Q2xkeXJXOSIsImlhdCI6MTYxOTE4MDU3MH0.GCUIfylVF5m8IxLHbUf0AJtZ4LPAgLtLEvPLImkqXgE"

requests.post(url, 
              headers={'Authorization': API_Key},
              files=[('upload', open(filepath))],
              verify = False, 
              data={"package_id":"822c5b77-a4eb-4175-80c3-95e9f657955b", "name":"test123"}
              )