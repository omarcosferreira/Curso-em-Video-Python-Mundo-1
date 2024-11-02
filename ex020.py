# from random import shuffle
import random
a1 = str(input(' digite o primeito nome: '))
a2 = str(input('digite o segundo nome: '))
a3 = str(input('digite o terceiro nome: '))
a4 = str(input('digite o quarto nome: '))

lista = [a1, a2, a3, a4]
#Embaralhar
random.shuffle(lista)
print('A ordem de apresentação será: ')
print(lista)