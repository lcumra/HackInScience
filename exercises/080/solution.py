# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import itertools
ciao = list(itertools.combinations('abcdefghijklmnopqrstuvwxyz', 2))
lungo = len(ciao)

for i in range(0, lungo - 1):
    print(ciao[i][0]+ciao[i][1])
