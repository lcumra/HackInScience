# -*- coding: utf-8 -*-
"""
Created on Thu Sep 24 10:05:21 2015

@author: pippo
"""

import json

with open("velib.json") as jj:
    d = json.load(jj)

for i in d:
    i['city'] = i['city'[:8]]