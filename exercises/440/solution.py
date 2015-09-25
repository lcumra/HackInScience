# -*- coding: utf-8 -*-
"""
Created on Fri Sep 25 17:42:49 2015

@author: pippo
"""


def filtered(items, cacca):
    out = []
    for i in range(len(items)):
        if cacca(items[i]):
            out.append(items[i])
    return out

if __name__ == '__main__':
    x1 = filtered(range(0, 101), lambda x: x % 3 == 0)
    print(', '.join(str(e) for e in x1))
    x2 = filtered(range(0, 101), lambda x: x % 5 == 0)
    print(', '.join(str(e) for e in x2))
    x3 = filtered(range(0, 101), lambda x: x % 15 == 0)
    print(', '.join(str(e) for e in x3))
