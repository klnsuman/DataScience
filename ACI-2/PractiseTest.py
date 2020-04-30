#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar  6 20:00:49 2020

@author: klrao
"""

from collections import defaultdict

d = defaultdict(list)
d['python'].append("awesome")

print(d)

'''l = 1,2,3

print(l)
print(l[1])

l = ((1,'a'),(2,'b'),(3,'c'))

print(l)
print(l[1])

for i,j in l:
    print(i,j)'''
    
l = [[1,'a'],[2,'b'],[3,'c']]
for i,j in l:
    print(i,j)
    
    


name = [ "Manjeet", "Nikhil", "Shambhavi", "Astha" ] 
roll_no = [ 4, 1, 3, 2 ] 
marks = [ 40, 50, 60, 70 ] 
  
# using zip() to map values 
mapped = zip(name, roll_no, marks) 

mapped = list(mapped) 
print(mapped)
  

name = [ "Manjeet", "Nikhil", "Shambhavi", "Astha" ] 
roll_no = [ 4, 1, 3, 2 ] 
marks = [ 40, 50, 60, 70 ] 
  
# using zip() to map values 
mapped = zip(name, roll_no, marks) 
mapped = set(mapped) 
print("set mapped",mapped)