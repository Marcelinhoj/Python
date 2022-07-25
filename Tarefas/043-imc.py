print('\033[1;33m====\033[m' * 10)
m = float(input('Digite sua massa corporal: Kg '))
a = float(input('Digite sual altura: '))
print('\033[1;33m====\033[m' * 10)

imc = m/(a**2)

if imc< 18.5:
    print('Seu imc é {:.2f} .. \033[7mABAIXO DO PESO \033[m'.format(imc))
if imc>18.4 and imc<25:
    print('Seu imc é {:.2f} .. PESO IDEAL'.format(imc) )
elif imc>24.9 and imc<30:
    print('Seu imc é {:.2f} .. SOBREPESO'.format(imc))
elif imc>29.9 and imc<40:
    print('Seu imc é {:.2f} .. OBESIDADE'.format(imc))
elif imc>39.9:
    Print('Seu imc é {:.2f} .. OBESIDADE MORBIDA'.format(imc))

print('\033[1;33m=-=-=\033[m' * 10)