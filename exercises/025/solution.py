# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import datetime
data = datetime.datetime.today()
anno = data.strftime("%Y-%m-%d")
ora = data.strftime("%H:%M:%S")

print("Today is ", anno, " and it is ", ora)
