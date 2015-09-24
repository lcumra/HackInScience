# -*- coding: utf-8 -*-
"""
Created on Thu Sep 24 10:05:21 2015

@author: pippo
"""

import json


def load_json(j):
    with open(j) as jj:
        d = json.load(jj)
    return d
