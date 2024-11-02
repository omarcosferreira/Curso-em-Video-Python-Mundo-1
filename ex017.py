'''co = float(input('Comprimento do cateto oposto: '))
ca = float(input('Comprimento do cateto adjacente: '))
hipotenusa = (co ** 2 + ca ** 2) **(1/2)
print('A hipotenusa vai medir {:.2f}'.format(hipotenusa))'''

from math import hypot
co = float(input('comprimento do ceteto oposto: '))
ca = float(input('Comprimento do ceteto adjacente: '))
hipotenusa = hypot(co, ca)
print('A hipotenusa vai medir {:.2f}'.format(hipotenusa))