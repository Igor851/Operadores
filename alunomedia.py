# -*- coding: utf-8 -*-
"""AlunoMedia.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1lGLWOUj9YWdjWDruRLD6TrOLZkgZyNdz
"""

aluno = input('digite o nome do aluno: ')
n1 = float(input('digite a primeira nota:'))
n2 = float(input('digite a segunda nota:'))
n3 = float(input('digite a terceira nota:'))
media = ((n1 + n2 + n3) / 3)

print(f'A média do aluno é {media}')

if ( media <= 4) :
  situacao = 'reprovado'
elif (media >=4 and media <= 7):
  situacao = 'recuperação'
elif (media >= 7):
  situacao = 'aprovado'


print(f'o {aluno} tem a média de {media} e foi {situacao}')