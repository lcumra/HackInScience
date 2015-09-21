# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import datetime
data = datetime.datetime.today()

#from time import gmtime, strftime
 #strftime("%a, %d %b %Y %H:%M:%S +0000", gmtime())

print("Today is ", datetime.date.today(), " and it is ", data.strftime("%H:%M:%S"))
