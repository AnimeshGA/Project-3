# -*- coding: utf-8 -*-
"""
Created on Sat Jul 17 20:40:48 2021

@author: Royal
"""

W= input('Please enter a string ')
def most_frequent(string):
    d = dict()
    for key in string:
        if key not in d:
            d[key] = 1
        else:
            d[key] += 1
    return d
print (most_frequent(W))
