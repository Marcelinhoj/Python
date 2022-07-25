km = int(input('\033[1;32mQual a distancia de sua viagem? km\033[m  '))
print('Você esta preste a começar uma viagem de {} km.'.format(km))
if km<=200:
    viagem = km*0.50
else:
    viagem = km*0.45
print(' A viagem custará \033[1;31;40mR$ {:.2f}\033[m reais. '.format(viagem))

'''viagem = km*0.50 if km <= 200 else viagem = km*045 '''
