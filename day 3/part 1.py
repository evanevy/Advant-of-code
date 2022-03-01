# -*- coding: utf-8 -*-
"""
Created on Thu Jan 27 22:55:13 2022

@author: evanevy
"""

path = open("day3.txt", "r")
data = path.read().splitlines()
path.close()
l =[]
for ele in range(len(data[0])):
    l.append("")
    
for ele in range(len(data)):
    for num in range(len(data[ele])):
        l[num] += data[ele][num]

        

gamma_binary = ""
epsilon_binary = ""
for ele in range(len(l)):
    if l[ele].count("1")>l[ele].count("0"):
        gamma_binary += "1"
        epsilon_binary += "0"
    else:
        gamma_binary += "0"
        epsilon_binary += "1"
gamma_decimal = 0
epsilon_decimal = 0

n = len(data[0])-1
ele = 0
while n>= 0 :
    
    gamma_decimal += int(gamma_binary[ele])*(2**n)
    epsilon_decimal += int(epsilon_binary[ele])*(2**n)
    ele += 1
    n -= 1
    
print(gamma_binary, epsilon_binary)
print(gamma_decimal, epsilon_decimal)
print(gamma_decimal*epsilon_decimal)
    
    
        