largura = float(input('Digite a largura em metros da sua parede: '))
altura = float(input('Digite a altura em metros da sua parede: '))
area = largura * altura
litro = area / 2
print('A sua altura é igual a {:.2f} metros, e a sua largura é igual a {:.2f} metros'.format(altura, largura))
print('Essas medidas resultam em uma área total de {:.2f} metros quadrados'.format(area))
print(' Considerando que cada 2 litros de tinta consegue pintar uma área igual a 2m², serão usadas {:.2f} litros de tinta para pintar essa parede de {:.2f}m²'.format(litro,area))
 