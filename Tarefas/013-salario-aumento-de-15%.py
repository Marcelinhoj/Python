print('======================')
nome1 = input('Nome do funcionário ?: ')
salario = float(input(' Qual seu salário atual ?: R$  '))
aumento = (salario*15)/100
salatual = salario + aumento
print('==========================================================================================================')
print( '{} voce teve um aumento de R$ {:.2f} reais, e seu novo salario é R$ {:.2f} reias.'.format(nome1,aumento,salatual)) 
print('==========================================================================================================')