n1 = float(input('digite a primeira nota: '))
n2 = float(input('digite a segunda nota: '))
media = (n1 + n2)/2
if media >= 6:
    print('Parabens! As sua media foi {:.1f}'.format(media))
else:
    print('A sua media foi {:.2}, estude mais!'.format(media))
