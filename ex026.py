"""frase = str(input('digite uma frase'))
print("letra A se repete ",frase.count('a')," vezes")
print('posição da primeira letra A é ', frase.find('a'))
"""
from pydoc import stripid

frase = str(input('digite uma frase: ')).upper().strip()
print('a letra A aparece {} vezes na frase.'.format(frase.upper().count('A')))
print('a  primeira letra A esta na posição {}.'.format(frase.find('A') +1 ))
print('a ultima posição da letra A é {}'.format(frase.rfind('A') +1 ))
