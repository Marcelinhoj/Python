from random import randint
from time import sleep # FAZ ESPERAR UM POUCO
computador = randint(0, 5)  # FAZ O COMPUTADOR PENSAR
print('-=-' *20)
print('Vou pensar em um número entre 0 e 5 .Tente advinhar...')
print('--=' *20)
jogador = int(input('Em que número pensei: ')) # JOGADOR TENTA ADVINHAR
print('Processando...')
sleep(3)
if jogador == computador:
    print('Você me venceu. PARABÉNS!!!')
else:
    print('Ganhei! Eu pensei no número {} e não no {} !!'.format(computador,jogador))