salario = float(input('qual seu salario? '))
if salario >1250:
    print('o seu salario de R${:.2f},\nteve um aumento de 10% ficando igual a R${:.2f}'.format(salario, (salario *1.10)))
else:
    print('o seu salario de R${:.2f}, \nteve um aumento de 15% ficando igual a R${:.2f}'.format(salario, (salario *1.15)))
