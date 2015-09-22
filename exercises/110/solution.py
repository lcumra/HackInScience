# -*- coding: utf-8 -*-
"""
Created on Tue Sep 22 15:34:44 2015

@author: pippo
"""
import sys
comandi = ['+', '-', '\*', '//', '%', '^']

if len(sys.argv) == 4:
    b = sys.argv[2]
    try:
        a = int(sys.argv[1])
        c = int(sys.argv[3])
        if b in comandi:
            if b == '+':
                d = a + b
            elif b == '-':
                d = a - b
            elif b == '\*':
                d = a * b
            elif b == '//':
                d = a / b
            elif b == '%':
                d = a % b
            else:
                d = a ** b
            print(d)
        else:
            print('input error')
        #break
    except:
        print("input errore")
else:
    print('usage: ./solution.py a_number (an_operator +-*/%^) a_number')
