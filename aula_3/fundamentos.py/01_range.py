#range(): função que gera uma faixa de números
#é muito usada em associação com listras

#range() com 1 armento: gera uma lista que vai de 0 até argument0 -1

for x in range(10):
    print(x)

print('_' *80)

#range() com 2 argumentos: gera uma lista começando 
#pelo primeiro argumento (inclusive) ate o segundo argumento (exclusive)

for y in range (5,15):
    print(y)

print('_' *80)

#range() com três argumentos:
# 1º: limite inferior (inclusive)
# 2º: limeite superior (exclusive)
# 3º: passo (de quando em quanto a lista vai andar; pode ser negativo)

for z in range (0, 22, 3): #gera lista de 0 a 21, daltando de 3 em 3
    print(z)

print('_' *80)

#range() com passo negativo
for k in range(10, 0, -1): #contagem regressiva de 10 a 1
    print(k)

