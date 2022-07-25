print('\033[2;33;40mx-x-x-\033[m' *20)
km = float(input('Qual a velocidade atual do carro? '))
multa = (km-80) * 7
if km > 80:
    print('\033[1;32;45mMULTADO !!! \033[mVocê ultrapassou o limite de \033[1;30;40m80 km\033[m permitido.')
    print('Sua multa é de R$ {} reais. '.format(multa))
print('Tenha um bom dia ! DIRIJA com segurança.. ')