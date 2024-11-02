import random
tenta = int(input('adivinhe o numero aleatorio entre 0 e 5: '))
numeroaleatorio = random.randint(0, 5)
if tenta==numeroaleatorio:
    print('parabens voce acertou, no numero aleatorio é {:.1f}'.format(numeroaleatorio))
else:
    print('voce errou o numero aleatorio é {:.2f}'.format(numeroaleatorio))

