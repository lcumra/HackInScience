# -*- coding: utf-8 -*-
"""
Created on Fri Sep 25 15:41:57 2015

@author: pippo
"""

from geopy import Nominatim
geo = Nominatim()
location = geo.reverse("40.851775, 25.268124")
print(location.address)
#Nominatim.reverse()

