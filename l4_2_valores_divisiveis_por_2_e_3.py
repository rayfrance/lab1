# -*- coding: utf-8 -*-
"""l4_1_valores_divisiveis_por_2_e_3.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1ussqCTbi793iL7dMGmDjuRce2dSikxGM
"""

inicio = int(input())
fim = int(input())

for i in range(inicio, fim+1):
  if (i%2 == 0 or i%3 == 0):
    print(i)