# -*- coding: utf-8 -*-
"""
Created on Tue Sep 22 17:27:14 2015

@author: pippo
"""
import isprime
a = 0

for i in range (2, 1000):
    if isprime.is_prime(i):
        a =+ i

print (a)
