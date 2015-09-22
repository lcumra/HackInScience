# -*- coding: utf-8 -*-
"""
Created on Mon Sep 21 18:56:59 2015

@author: pippo
"""
from operator import *

def sort_a_list(lista):
    print(sorted(lista, revrese=True))
    return;

def sort_by_mark(mycl):
    print(sorted(mycl, key=itemgetter(1), reverse=True))
    return;

def sort_by_name(mclass):
    print(sorted(mclass, key=itemgetter(2)))
    return;
