# -*- coding: utf-8 -*-
"""
Created on Thu Sep 24 15:15:50 2015

@author: pippo
"""
import string
al = list(string.ascii_lowercase)


def numa(x):
    for i in range(0, len(al)):
        if x == al[i]:
            return i
    else:
        return 666
