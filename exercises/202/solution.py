# -*- coding: utf-8 -*-
"""
Created on Tue Sep 22 16:48:26 2015

@author: pippo
"""


def is_alpha(al, top):
    allist = list(al)
    toplist = list(top)
    x = True
    for i in range(1, len(toplist)):
        if allist[i] not in toplist[i]:
            x = False
            return x
    return x
