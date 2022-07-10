#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar  7 20:40:43 2019

@author: risavchd24
"""

case = int(input())
for _ in list(range(case)) :
    a,b = [int(x) for x in input().split()]
    s = [int(y) for y in range(1,b+1)]
    for i in range(1,b-1) :
        for j in range(i+1,b) :
            if int(s[i]) != 1 and int(s[j])%int(s[i]) == 0 :
                s[j] = 1
    for k in range(a-1,b) :
        if int(s[k]) != 1 :
            print(s[k])
            


@@@@ dsklfnklasdfnlsfnidfio jofdfnsifioefioasn *************8
hanuman
