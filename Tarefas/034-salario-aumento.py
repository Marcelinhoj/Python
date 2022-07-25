sal = float(input('Informe seu salário atual: R$ '))
if sal>=1250 :
    novosal = (sal*10)/100 + sal
else:
    novosal = (sal*15)/100 + sal
print('Seu novo salário sera é de R$ {:.2f} reais'.format(novosal))