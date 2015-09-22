# -*- coding: utf-8 -*-
"""
Created on Mon Sep 21 20:19:33 2015

@author: pippo
"""

import string
ciao = string.ascii_lowercase

b = 1
for i in range(0, 25):
    for j in range (b, 26):
        print(ciao[i]+ciao[j])
    b = b + 1
    