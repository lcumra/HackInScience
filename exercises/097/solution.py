# -*- coding: utf-8 -*-
"""
Created on Mon Sep 21 18:56:59 2015

@author: pippo
"""
meet = list

def love_meet(a, b):
    alen = len(a)
    blen= len(b)
    for i in range(0, alen):
        for j in range(0, blen):
            if a[i] is b[j]:
                meet.append(a[i])
    return meet
