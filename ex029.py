velocidade = int(input('digite a velocidade: '))
if velocidade> 80:
    print('voce foi multado por exceder a velocidade de 80km, \n vai pagar uma multa ')
    print('multa no valor de 7 reais por cada km excedente')
    print('sua multa ficou no valor de {:.2f}'.format((velocidade -80)*7))
else:
    print('sua velocidade foi de {: .1f}km como voce nao excedeu 80 km, não sera multado'.format(velocidade))
