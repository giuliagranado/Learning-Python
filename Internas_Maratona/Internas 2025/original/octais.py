# -*- coding: utf-8 -*-
"""
Created on Sat Nov  1 11:04:17 2025

@author: lab54
"""

# parte do aquecmento pré-maratona

k = int(input())
continues = True
numero = []
palindrome = True

while continues:
    num = divmod(k,8)
    k = num[0]
    remainder = num[1]
    if k == 0:
        break
    numero.append(remainder)


for i,x in enumerate(numero):
    if x != numero[len(numero)-(1+i)]:
        palindrome = False
        break

if palindrome:
    print("S")
else:
    print("N")
    
