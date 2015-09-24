# -*- coding: utf-8 -*-
"""
Created on Thu Sep 24 10:05:21 2015

@author: pippo
"""

import json

with open("velib.json") as jj:
    d = json.load(jj)

le = len(d)
pr = [0] * le
prr = [0] * le
ii = [0] * le
for i in range(0, le):
    d[i]['name'] = d[i]['name'][8:]
    ii[i] = i
    pr[i] = d[i]["address"].split(" - ")
    prr[i] = pr[i][1].split(" ")
    d[i]['address'] = pr[i][0]
    d[i].update({'city' : prr[i][1]})
    d[i].update({'zip_code' : prr[i][0]})
