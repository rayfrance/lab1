# -*- coding: utf-8 -*-
"""l4_1_urna_eletronica(1).ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1XcFb2c_cKuJaEoQvSFwgutSB4eA6BWd0
"""

eleitores = int(input())

i=0
quantidade_candidato1=0
quantidade_candidato2=0
quantidade_candidato3=0
quantidade_candidato4=0
contagem_nulos=0

quantidade_total = 0
candidato = 0

while (i< eleitores and candidato != 'sair'):
  candidato = input()
  if (candidato.strip() == '1'):
      quantidade_candidato1+=1
  elif (candidato.strip() =='2'):
      quantidade_candidato2+=1
  elif (candidato.strip() =='3'):
       quantidade_candidato3+=1
  elif (candidato.strip() =='4'):
      quantidade_candidato4+=1
  else:
      if (candidato.strip() != 'sair'):
        contagem_nulos+=1
  i+=1
  if (candidato != 'sair'):
    quantidade_total+=1

  if (quantidade_total == 0):
    quantidade_total = 1

  porcentagem_candidato1 = quantidade_candidato1*100/quantidade_total
  porcentagem_candidato2 = quantidade_candidato2*100/quantidade_total
  porcentagem_candidato3 = quantidade_candidato3*100/quantidade_total
  porcentagem_candidato4 = quantidade_candidato4*100/quantidade_total
  porcentagem_nulo = contagem_nulos*100/quantidade_total

candidato1 = 'José Alfredo'
candidato2 = 'Maria Junqueira'
candidato3 = 'Marivaldo Silva'
candidato4 = 'Juliana Antônia'

print(f'Nome--------------Votos--------------Porcentagem')
print(f'{candidato1} ------ {quantidade_candidato1} ------------------- {porcentagem_candidato1:.2f}%')
print(f'{candidato2} --- {quantidade_candidato2} ------------------- {porcentagem_candidato2:.2f}%')
print(f'{candidato3} --- {quantidade_candidato3} ------------------- {porcentagem_candidato3:.2f}%')
print(f'{candidato4} --- {quantidade_candidato4} ------------------- {porcentagem_candidato4:.2f}%')
print(f'Nulo -------------- {contagem_nulos} ------------------- {porcentagem_nulo:.2f}%')