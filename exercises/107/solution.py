# -*- coding: utf-8 -*-
"""
Created on Tue Sep 22 12:24:14 2015

@author: pippo
"""
from operator import *


def select_student(l, tr):
    llen = len(l)
    acc = list()
    ref = list()
    for i in range(0, llen):
        if l[i][1] >= tr:
            acc.append(l[i])
        else:
            ref.append(l[i])
    resu = {'Accepted': sorted(acc, key=itemgetter(1)),
            'Refused': sorted(ref, key=itemgetter(1), reverse=True)}
    return resu
