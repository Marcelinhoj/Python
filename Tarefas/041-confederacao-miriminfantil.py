print('\033[1;35;43m++==--\033[m'*6)
print('\033[1;31m  CONFEDERAÇÃO NACIONAL DE NATAÇÃO\033[m')
print('\033[1;35;43m++==--\033[m'*6)
ano = int(input('Ano de nascimento do atleta:  '))

idade = 2022 - ano

if idade<10:
    print('Atleta com {} anos : MIRIM'.format(idade))

if idade>9 and idade<15:
    print('Atleta com {} anos : INFANTIL '.format(idade))

elif idade>14 and idade<20:
    print('Atleta com {} anos : JUNIOR'.format(idade))

elif idade>19 and idade<21:
    print('Atleta com {} anos : SÊNIOR '.format(idade))

elif idade>20:
    print('Atleta com {} anos : MASTER'.format(idade))

print('\033[1;35;43m++==--\033[m'*6)
