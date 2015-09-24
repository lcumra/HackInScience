# -*- coding: utf-8 -*-
"""
Created on Thu Sep 24 14:00:35 2015

@author: pippo
"""

li1 = []
li2 = []


def draw_n_squares(n):
    carre1 = ('+---+')
    carre2 = ('|   |')
    for i in range(0, n):
        li1.append(carre1)
        li2.append(carre2)
    l1 = ''.join(li1)
    l2 = ''.join(li2)
    ciao = (l1 + '\n' + l2 + '\n' + l1 + '\n')
    ciaone = []
    for i in range(0, n):
        ciaone.append(ciao)
    return ''.join(ciaone)
