
from datetime import date
ano = int(input('digite o ano: '))
if ano ==0:
    ano = date.today().year
resto=ano %4
#print(resto)
#if resto == 0:
if ano % 4 == 0 and ano %100 != 0 or ano %400==0:
    print('O ano de {:.0f} é bissexto.'.format(ano))
else:
   print('o ano de {:.0f}, não é bissexto'.format(ano))

