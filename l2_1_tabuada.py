# -*- coding: utf-8 -*-
"""l2-1 tabuada.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1wAcwBDl48LODVDnRQCDu2qCyuH0E5uDV
"""

n = int(input())
tabuada = [];
for i in range(1,11):
  elem = n * i
  tabuada.append(elem)
  print(f"{n} x {i} = {tabuada[i-1]}")