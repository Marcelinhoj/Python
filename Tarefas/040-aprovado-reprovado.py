print('\033[7m++==--\033[m'*5)
a = float(input('Primeira nota: '))
b = float(input('Segunda nota: ')) 
print('\033[7m++==--\033[m'*5)

media = (a + b)/2

if media<5:
    print('Sua média foi \033[1;31m{:.2f} .REPROVADO\033[m !!'.format(media))

elif media>=5 and media<6.9:
    print('Sua media foi \033[1;33m{:.2f} . RECUPERAÇÃO\033[m !!'.format(media))

else:
    print('Sua média foi \033[1;34m{:.2f} . APROVADO \033[m!!'.format(media))