# -*- coding: utf-8 -*-
"""
Created on Sat Oct 10 10:17:00 2020

@author: chmaa
"""

a=float(input("Digite a nota do 1º Bimestre:"))
b=float(input("Digite a nota do 2º Bimestre:"))
c=float(input("Digite a nota do 3º Bimestre:"))
d=float(input("Digite a nota do 4º Bimestre:"))

media = (a+b+c+d)/4

print("\nA Média das notas é:", media)
print("\nA Média das notas é:{:04.1f}".format (media))