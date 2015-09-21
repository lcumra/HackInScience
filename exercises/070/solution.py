# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import string
import itertools
#ciao = list(string.ascii_lowercase)
ciao = list(itertools.combinations('abcdefghijklmnopqrstuvwxyz', 2))
lungo = len(ciao)

for i in range(0, lungo - 1):
    print(ciao[i][0]+ciao[i][1])
