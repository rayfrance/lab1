# -*- coding: utf-8 -*-
"""l6_2_somando_matrizes.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1QFPHR_EP8N22ebI5mHdQgaei9N7eLO_7
"""

import numpy as np

lista1 = []
lista2 = []

for i in range(9):
  x = int(input())
  lista1.append(x)

for i in range(9):
  x = int(input())
  lista2.append(x)

matriz1 = np.array(lista1).reshape(3,3)
matriz2 = np.array(lista2).reshape(3,3)
matriz_soma = matriz1 + matriz2

saidas1 = [lista1[0:3],lista1[3:6],lista1[6:9]]
saidas2 = [lista2[0:3],lista2[3:6],lista2[6:9]]
soma = matriz_soma.tolist()

print(saidas1)
print(saidas2)
print(soma[0])
print(soma[1])
print(soma[2])