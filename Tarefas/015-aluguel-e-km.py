print('========================')
dia = int(input(' Quantos dias alugados? '))
km = float(input('Quantos km rodados ? '))
d = dia * 60
k = km * 0.15
alu = d + k

print('========================')
print(' O total a pagar é de R$ {:.2f} .'.format(alu))
