####from random import choice
import random

a1 = str(input(" insira no nome do primeiro aluno "))
a2 = str(input('insira o nome do segundo aluno '))
a3 = str(input('insira o nome do terceiro aluno '))
a4 = str(input('insira o nome do querto aluno '))
lista = [ a1, a2, a3,a4 ]
escolhido = random.choice(lista)
print('O aluno escolhido é o {}'.format(escolhido))
