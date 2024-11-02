salario = float(input('Insira o valor do salario: '))
#aumento = salario + (salario * 15/100)
aumento = salario * 1.15
s15 = salario * 0.15
# s15 = salario * 15/100
print('O seu salario de R${:.2f}, teve um aumento de 15% (R${:.2f}), totalizando R${:.2f} de salario.'.format(salario, s15,aumento))
