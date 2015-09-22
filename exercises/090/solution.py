# -*- coding: utf-8 -*-
"""
Created on Mon Sep 21 18:56:59 2015

@author: pippo
"""
import sys

lista = list(enumerate(sys.argv))
a = len(lista)

for i in range(0, a):
    print(i, sys.argv[i])
