# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
a = 0
b = 0
for i in range(1, 1000):
    if i % 3 == 0:
        b = b + i
    if i % 5 == 0:
        a = a + i
print(a + b)        
