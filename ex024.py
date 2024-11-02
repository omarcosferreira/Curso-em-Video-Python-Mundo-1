nome = str(input('Digite o nome da cidade: ')).strip()

nome= nome.upper()
print('o nome da cidade tem a palavra santo? ')
print('SANTO' in nome)
print('o nome da cidade começa com a palavra Santo?')
print('SANTO' in nome[:5])

cid = str(input('Em que cidade você nasceu? ')).strip()
print(cid[0:5].upper() == 'SANTO')


