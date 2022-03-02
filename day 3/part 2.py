# -*- coding: utf-8 -*-
"""
Created on Fri Jan 28 14:18:19 2022

@author: evanevy
"""

path = open("day3.txt", "r")
data = path.read().splitlines()
path.close()

poss_val = data
lst_col_bin = []

def gen_col_bin_O2 (my_list): 
    l = []
    for ele in range(len(my_list[0])):
        l.append("")   
    for ele in range(len(my_list)):
        for num in range(len(my_list[0])):
            l[num] += my_list[ele][num]
            
    return l
       
def get_rating(any_list, mode = "oxygen"):        
    ele = 0
    l = data        
    l2 = lst_col_bin
    while len(l) >1:
        temp_list = []
        if l2[ele].count("1") >= l2[ele].count("0"):
            for item in l:
               if mode == "oxygen":
                   if item[ele] == "1":
                       temp_list.append(item)
               elif mode == "CO2":
                   if item[ele] == "0":
                       temp_list.append(item)
        else:
            for item in l:
                if mode == "oxygen":
                    if item[ele] == "0":
                        temp_list.append(item)
                elif mode == "CO2":
                    if item[ele] == "1":
                        temp_list.append(item) 
        l = temp_list
        
        l2 = gen_col_bin_O2(temp_list)
        ele += 1
    return l

def conv_bin_to_dec(binary):
    decimal = 0
    n = len(binary[0])-1
    ele = 0
    while n>= 0 :
        
        decimal += int(binary[0][ele])*(2**n)
        ele += 1
        n -= 1
    return decimal
    

lst_col_bin = gen_col_bin_O2(data)

x = get_rating(data, "oxygen")
y= get_rating(data, "CO2")  
print(x)
print(y) 
print(conv_bin_to_dec(x)*conv_bin_to_dec(y))
           
        
        
