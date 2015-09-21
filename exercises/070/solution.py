# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import string
ciao = list(string.ascii_lowercase)

for i in range(0, 26):
    for j in range(0, 26):
        if i != j:
            print(ciao[i] + ciao[j])
