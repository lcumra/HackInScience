# -*- coding: utf-8 -*-
"""
Created on Tue Sep 22 17:46:20 2015

@author: pippo
"""

import requests 

try:
    r = requests.get('http://mdk.fr/ip')
    print(r)
except ConnectionError as conny:
    print('No internet connectivity.')
