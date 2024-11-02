n = str(input("digite um nome:")).strip()
nome = n.split()
print("primeiro nome: {}".format(nome[0]))
print('o ultimo nome é {}.'.format(nome[len(nome) -1]))
