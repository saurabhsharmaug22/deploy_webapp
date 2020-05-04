# -*- coding: utf-8 -*-
"""
Created on Mon May  4 16:49:32 2020

@author: HP
"""


import requests
url = 'https://localhost:5000/request_api'
pred = requests.post(url,json={'age':55, 'sex':'male', 'bmi':59, 'children':1, 'smoker':'male', 'region':'northwest'})
print(pred.json())