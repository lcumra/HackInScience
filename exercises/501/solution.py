# -*- coding: utf-8 -*-
"""
Created on Thu Sep 24 17:12:09 2015

@author: pippo
"""


def recMC(resto, lista):
   minCoins = resto
   if resto in lista:
     return 1
   else:
      for i in [c for c in lista if c <= resto]:
         numCoins = 1 + recMC(lista, resto - i)
         if numCoins < minCoins:
            minCoins = numCoins
   return minCoins
