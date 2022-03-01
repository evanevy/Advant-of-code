# -*- coding: utf-8 -*-
"""
Created on Sat Jan 29 09:32:14 2022

@author: evane
"""
import math
path = open("day4.txt")
data = path.read().split("\n\n")
path.close()

loto_num = data[0]
num_of_matrix = len(data)-1

pre_matrix = data[1:]

for ele in range(len(pre_matrix)):
    pre_matrix[ele] = pre_matrix[ele].split()




matrix_dict = {}
for ele in range(len(pre_matrix)):
    matrix_dict[ele] = pre_matrix[ele]

    
def create_grid(dict_key):
    pre_grid = matrix_dict[dict_key]
    n = int(math.sqrt(len(pre_matrix[0])))
    l = []
    for num in range(0,len(pre_grid),n):
        l.append(pre_grid[num:num+5])

    return l

def gen_vertical_list(matrix):
    l = []
    for ele in range(len(matrix)):
        l.append([])
    for ele in range(len(matrix[0])):
        for num in range(len(matrix[0])):
            l[num].append(matrix[ele][num])
    return l
for ele in range(len(pre_matrix)):
    matrix_dict[ele] = create_grid(ele)
for ele in range(len(matrix_dict)):
    matrix_dict[ele] = matrix_dict[ele], gen_vertical_list(matrix_dict[ele])

def check_for_0(matrix_dict):
    for ele in range(len(matrix_dict)):
        for num in range(len(matrix_dict[ele])):
            for x in range(len(matrix_dict)[ele][num]):
                return sum(matrix_dict[ele][num][x]) == 0


print(matrix_dict.items())
print(loto_num)
print()


            
            
    