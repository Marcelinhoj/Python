print('\033[1;37;43m==-==-\033[m'*5)
print('\033[7m      BANCO TO QUEBRADO      \033[m')
print('\033[1;37;43m==-==-\033[m'*5)

# Informações
casa = float(input('Qual o valor da \033[7mCasa\033[m ? R$ '))
salario = float(input('Qual o seu salário? R$  '))
anos = int(input('Em quanto anos gostaria de pagar? '))
print('\033[1;37;43m==-==-\033[m'*5)


# tabela
prestacao = anos *12
custo = casa / prestacao
dasim = (salario*30)/100


if custo>dasim:
     print(' Vai ter {} parcelas, cada uma custando R$ {:.2f}.'.format(prestacao,custo))
     print(' Devido ao valor das parcelas exeder 30% do seu salario é \033[7mR${} \033[m.Seu emprestimo foi recusado. '.format(dasim))
else:
    print(' Vai ter {} parcelas, cada uma custando \033[7mR$ {:.2f}\033[m.'.format(prestacao,custo))
    print('Parabéns pelo envestimento')
print('\033[1;33;44mTenha um otimo dia!!\033[m')





