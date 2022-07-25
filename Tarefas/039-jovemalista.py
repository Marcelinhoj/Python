print('\033[7mx-x-x-x-\033[m'*5)
ano = int(input('Digite o ano de seu nascimento: '))
print('\033[7mx-x-x-x-\033[m'*5)

idade = 2022 - ano
falta = 18 - idade

if idade<18:
    print(' Com a idade de {} anos, ainda vai ter que esperar {} anos para se alistar.'.format(idade,falta))

elif idade == 18:
    print(' Com {} anos, é a hora exata de se alistar.'.format(idade))

elif idade>18:
    print('Com {} anos, ja passou da idade certa de se alistar.'.format(idade))
