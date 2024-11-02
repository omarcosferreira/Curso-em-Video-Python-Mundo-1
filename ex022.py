"""nome = str(input('Digite o nome completo: '))
print('nome com letras maiusculas: ', nome.upper())
print('nome com letras minisculas: ', nome.lower())
#print(nome.split().len(nome))
nome = nome.split()
#print(len(nome))
print('quantas letras tem o primeiro nome: ', len(nome[0]))

print("""
#FEITO DE MANEIRA CORRETA!
""")
nome = str(input('digite o nome completo:'))
print('nome com todas as letras maiuscula: ', nome.upper() )
print('nome com todas as letras minusculas: ', nome.lower())
nome1 = nome.replace(' ', '')
print('quantas letras tem todo o nome: ', len(nome1))

nome = nome.split()

print('quantas letras tem o primeiro nome: ', len(nome[0]))
"""
print("""
Versão do professor guanabara""")
nome = str(input('Digite seu nome completo: ')).strip()
print('Analisando seu nome...')
print('Seu nome em maiúsculas é {}.'.format(nome.upper()))
print('Seu nome em minúsculas é {}.'.format(nome.lower()))
print("Seu nome tem ao todo {} letras.".format(len(nome) -nome.count(" ")))
print('Seu primeiro nome tem {} letras.'.format(nome.find(" ")))
separa= nome.split()
print("Seu primeiro nome é {} e ele tem {} letras.".format(separa[0], len(separa[0])))
