# -*- coding: utf-8 -*-
"""
Created on Tue Sep 22 16:48:26 2015

@author: pippo
"""


def starts_with(al, top):
    allist = list(al)
    toplist = list(top)
    x = True
    if len(allist) < len(toplist):
        return False
    for i in range(1, len(toplist)):
        if allist[i] not in toplist[i]:
            x = False
            return x
    return x
