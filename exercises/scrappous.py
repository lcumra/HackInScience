# -*- coding: utf-8 -*-
"""
Created on Thu Sep 24 11:21:31 2015

@author: pippo
"""

import requests
from bs4 import BeautifulSoup as bs
#import beautifulsoup as bs

url = "http://www.marmiton.org/recettes/recette_cassouflette-mix-cassoulet-tartiflette_331670.aspx"
result = requests.get(url)
if result.status_code == 200:
    soup = bs(result.text)
    print(soup.find("title").text)
