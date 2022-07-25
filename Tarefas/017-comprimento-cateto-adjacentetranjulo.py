import math
co = float(input(' Comprimento do cateto : '))
ca = float(input(' Comprimento do cateto adjacente: '))
hi = math.hypot(co, ca)
print(' A hipotenuza vai medir {:.2f} '.format(hi))



'''co = float(input('Qual o comprimento do cateto oposto: '))
ca = float(input('Qual o comrimento do catero adjacente:'))
hi = (co **2 + ca ** 2) **(1/2)
print(' A hipotenuza vai medir {:.2f} .'.format(hi))'''