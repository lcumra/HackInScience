# -*- coding: utf-8 -*-
"""
Created on Tue Sep 22 16:48:26 2015

@author: pippo
"""
import string
listone = list(string.ascii_letters)


def is_alpha(al):
    allist = list(al)
    x = True
    for i in allist:
        if i not in listone:
            x = False
            return x
    return x
