# -*- coding: utf-8 -*-
"""
Created on Tue Sep 22 17:33:37 2015

@author: pippo
"""
import isprime
s = ""
for i in range(10000, 100050):
    if isprime.is_prime(i):
        s += str(str(i) + ', ')
s[:-2]
print(s)
