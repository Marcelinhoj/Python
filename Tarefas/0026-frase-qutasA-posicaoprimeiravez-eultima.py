frase = str(input('Digite uma frase: ')).strip().upper()
print(' A letra A aparece {}'.format(frase.count('A')))
print('A primeira leta A apareceu na posição {}'.format(frase.find('A')+1))
print('A última letra A apareceu na posição {}'.format(frase.rfind('A')+1))