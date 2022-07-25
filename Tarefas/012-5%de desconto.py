print('==========================')
pat = float(input('Qual o valor do produto que você quer comprar?: '))
des = (pat*5)/100
real = pat - des
print('==========================')
print('==========================')
print(' Se você pagar a vista vai ter um desconto de R$ {:.2f} reais. '.format(des))
print(' E pagara R$ {:.2f} reais...' .format(real))
    