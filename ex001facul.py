idade = int(input('sua idade: '))
tempo_cnh = int(input('tempo de carteira: '))
aliquota = 0.05

if idade < 25:
    aliquota += 0.03
if tempo_cnh < 3:
    aliquota +=0.02

