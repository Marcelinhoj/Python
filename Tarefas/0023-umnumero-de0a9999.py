num = int(input('Informe um numero : '))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10
n = str(num)
print('Analisando o número {}'.format(num))
print('Unidade: {}'.format(n[3]))
print('Dezena : {}'.format(n[2]))
print('Centena: {}'.format(n[1]))
print('Milhar: {}'.format(n[0]))