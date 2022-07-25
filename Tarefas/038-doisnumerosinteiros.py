a = int(input('Digite o primeiro número: '))
b = int(input('Digite o segundo número: '))

if a>b:
    print('O primeiro valor {} é maior'.format(a))
elif b>a:
    print(' O segundo valor {} é maior'.format(b))
elif b==a:
    print('Não existe valor maior, os 2 sao iguais')