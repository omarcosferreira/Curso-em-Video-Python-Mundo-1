print('Para saber se um conjunto de medidas \nforma um triângulo, é preciso verificar \nse a soma dos dois lados menores é maior \nque o terceiro lado')
print("-=-="*10, "\n Analizador de Triângulos")
a = float(input('digite o valor do lado A do triângulo: '))
b = float(input('digite o valor do lado B do triângulo: '))
c = float(input('digite o velor do lado C do triângulo: '))
if a < b+c and b < a+c and c < a+b:
    print('\nEssas três reta PODEM formar um triângulo.')
else:
    print('\nessas retas NÃO podem formar um triângulo.')

