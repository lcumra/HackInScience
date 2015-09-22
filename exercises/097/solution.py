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
            if a[i] is b[j]:
                meet.append(a[i])
    return meet


def affair_meet(a, b, c):
    meet = list()
    alen = len(a)
    blen = len(b)
    clen = len(c)
    for i in range(0, alen):
        for j in range(0, blen):
            if a[i] is not b[j]:
                for k in range(0, clen):
                    if a[i] is c[k]:
                        meet.append(a[i])
    return meet
