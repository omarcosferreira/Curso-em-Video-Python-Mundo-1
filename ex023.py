"""numero = str(input('Insira um numero de 0 a 9999: '))
print('unidade: ', numero[3])
print('dezena: ', numero[2])
print('centena: ', numero[1])
print('milhar: ', numero[0])


numero= int(input('digite um numero de 0 a 9999: '))
num = str(numero)
print('unidade: ', num[3])
print('dezena: ', num[2])
print('centena: ', num[1])
print('unidade de milhar: ', num[0])"""
from inspect import formatannotation

num= int(input('digite um numero de 0 a 9999: '))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10
print('unidade:{}'.format(u))
print('dezena: {}'.format(d))
print('centena:{}'.format(c))
print('unidade de milhar:{}'.format(m))

