#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov  9 15:10:25 2026

@author: deck
"""

def isEven(number):
    return number % 2 ==0

user_input = int(input("whats the number?: "))
if isEven(user_input):
    print("even")
else:
    print("odd")