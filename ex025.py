nome= str(input('digite um nome: '))
print('a palavra Silva esta dentro desse nome? ')
print('Silva' in nome )

nome = str(input('Qual é seu nome completo? ')).strip()

print('voce tem Silva em seu nome: {}'.format('silva' in nome.lower()))
print('Voce tem silva como seu primeiro nome: {}'.format('SILVA' in nome[:5].upper()))

