# -*- coding: utf-8 -*-
"""
Created on Tue Sep 22 15:34:44 2015

@author: pippo
"""


def is_prime(m):
    check = 0
    x = True
    for i in range(2, m - 1):
        if m % i == 0:
            check += 1
    if check >= 0:
        x = False
    else:
        x = True
    return x
