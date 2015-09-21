# -*- coding: utf-8 -*-
"""
Created on Mon Sep 21 18:56:59 2015

@author: pippo
"""
import itertools
ciao = itertools.combinations('abcdefghijklmnopqrstuvwxyz', 2)

for i in ciao:
    print(i[0] + i[1])
    