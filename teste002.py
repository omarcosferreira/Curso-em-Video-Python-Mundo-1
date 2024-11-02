frase='Curso em Video Python'

print(frase[9])
print(frase[9:13])
print(frase[9:21])
print(frase[9:22:2])
print(frase[:5])
print(frase[15:])
print(frase[9::3])
print(len(frase))
'''conta quantas vezes a letra O se repete'''
print(frase.count('o'))
#Conta quantas vezes a letra O se repete dentro do espaço determinado
print(frase.count('o',0,13))
#mostra em qual posição começa os caracteres
#ele indica a posição
print(frase.find('deo'))
print(frase.find('so'))
# quando você usa a função find e os caracteres nao existem dentro da frase ele vai mostrar como resultado -1
print( frase.find('Android'))
print(frase.find('em'))
print( 'Curso' in frase)
print('andriod' in frase)
print(frase.replace('Python', 'Android'))
print(frase.upper())
print(frase.lower())
print(frase.capitalize())
print(frase.title())

frase= "   Aprenda Python  "
print(frase.strip())
print(frase.rstrip())
print(frase.lstrip())

frase= "Curso em Video Python"

"""o split ele divide uma strig 
em uma lista onde cada elemento 
vai ser definido pelo seu caractere 
de split, que por padrão vem o 'espaço'"""
print(frase.split())
print('-'.join(frase))
print(frase.upper().count('O'))
dividido = frase.split()
print(dividido)
print(dividido[0])
print(dividido[2])
print(dividido[2] [3])
frase= frase.replace('Python', 'Android')
print(frase)

