n1 = int(input('\033[0;40mdigite o primeiro numero a ser somado: \033[7;30;43m'))
n2 = int(input('digite o segundo numero a ser somado: '))
soma = n1 + n2
print('a soma dos numeros {} e {},\033[4;30;43m é igual a {}.\033[m'.format(n1, n2, soma))
