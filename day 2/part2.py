# -*- coding: utf-8 -*-
"""
Created on Thu Jan 27 09:42:17 2022

@author: Norberto Alves. 

"""

path = open("part1.txt", "r")
data = path.read().splitlines()
path.close()
h_counter = 0
d_counter = 0
a_counter = 0
for ele in data:
    if ele[0] == "f":
        h_counter += int(ele[-1])
        d_counter += a_counter * int(ele[-1])
    elif ele[0] == "d":
        a_counter += int(ele[-1])
    elif ele[0] == "u":
        a_counter -= int(ele[-1])
print(h_counter*d_counter)
