a = int(input('digite o primeiro numero: '))
b = int(input('digite o segundo numero: '))
c = int(input('digite o terceiro numero: '))
#Verificando quem é menor
menor = a
if b<a and b<c:
    menor = b
if c<b and c<a:
    menor = c
print("o menor valor digitado foi {}".format(menor))
maior = a
if b>a and b>c:
    maior = b
if c>a and c>b:
    maior = c
print('o maior valor digitado foi {}'.format(maior))
