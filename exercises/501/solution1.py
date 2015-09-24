# -*- coding: utf-8 -*-
"""
Created on Thu Sep 24 17:18:14 2015

@author: pippo
"""

def recMC(a, b):
    coinValueList = b
    change = a
    minCoins = change
    if change in coinValueList:
        return 1
    else:
        for i in [c for c in coinValueList if c <= change]:
            numCoins = 1 + recMC(coinValueList, change  -i)
            if numCoins < minCoins:
                minCoins = numCoins
    return minCoins
