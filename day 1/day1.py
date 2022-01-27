# -*- coding: utf-8 -*-
"""
Created on Thu Jan 27 09:42:17 2022

@author: Norberto Alves. 

"""

path = open("day1.txt", "r")
data = path.read().splitlines()
path.close()
for ele in range(len(data)):
    data[ele] = int(data[ele])
print(data)
depth_increase_counter = 0
for ele in range(1,len(data)):
    if data[ele] > data[ele-1]:
        depth_increase_counter += 1
print(depth_increase_counter)