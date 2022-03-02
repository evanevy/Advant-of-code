# -*- coding: utf-8 -*-
"""
Created on Thu Jan 27 09:42:17 2022

@author: Norberto Alves. evanevy 

"""

path = open("day1.txt", "r")
data = path.read().splitlines()
path.close()
for ele in range(len(data)):
    data[ele] = int(data[ele])
depth_increase_counter = 0
for ele in range(3,len(data)):
    if sum(data[ele-2:ele+1]) > sum(data[ele-3:ele]):
        depth_increase_counter += 1
print(depth_increase_counter)
