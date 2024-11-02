from math import cos, tan, radians, sin
angulo = float(input(' Digite o angulo: '))
seno = sin(radians(angulo))
cosseno = cos(radians(angulo))
tangente = tan(radians(angulo))
print('O angulo de {}º tem o seno de {:.2f}'.format(angulo,seno))
print('{}º tem o cosseno de {:.2f}'.format(angulo, cosseno))
print('{}º tem a tangente de {:.2f}'.format(angulo, tangente))
