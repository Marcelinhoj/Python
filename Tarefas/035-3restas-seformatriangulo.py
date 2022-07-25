print('\033[1;32moxoxox\033[m' * 8)
print('Analisador de triângulos')
print('\033[1;32moxoxox\033[m' * 8)
r1 = float(input('Primeiro segmento: '))
r2 = float(input('Segundo segmento: '))
r3 = float(input('Terceiro segmento: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os segmentos acima PODEM FOMAR triângulo!')
else:
    print('Os segmentos acima NÃO PODEM formar triãngulo')

print('\033[1;32moxoxox\033[m' * 10)