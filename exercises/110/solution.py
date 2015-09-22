# -*- coding: utf-8 -*-
"""
Created on Tue Sep 22 12:55:46 2015

@author: pippo
"""
import sys
comandi = ['+', '-', '\*', '//', '%', '^']

if len(sys.argv) > 3:
    def opera(a, b, c):
        if a.is_integer():
            if c.is_integer():
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
            else:
                print('input error')
        else:
            print('input error')
else:
    print('usage: ./solution.py a_number (an_operator +-*/%^) a_number')           
