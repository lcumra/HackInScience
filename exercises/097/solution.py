# -*- coding: utf-8 -*-
"""
Created on Mon Sep 21 18:56:59 2015

@author: pippo
"""


def love_meet(a, b):
    meet = list()
    alen = len(a)
    blen = len(b)
    for i in range(0, alen):
        for j in range(0, blen):
            if a[i] == b[j]:
                meet.append(a[i])
    return meet

    
def affair_meet(a, b, c):
    meet = list()
    alen = len(a)
    for i in range(0, alen):
        if a[i] in c and a[i] not in b:
            meet.append(a[i])
    return meet
