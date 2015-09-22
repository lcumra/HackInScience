# -*- coding: utf-8 -*-
"""
Created on Mon Sep 21 18:56:59 2015

@author: pippo
"""


def love_meet(a, b):
    meet = a.intersect(b)
    return meet


def affair_meet(b, a, c):
    meet = a.intersect(c)
    unmeet = meet.difference(b)
    return unmeet
