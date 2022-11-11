#lista
frutas = ["laranja", "maça", "uva", "pera", "mamão", "abacate", "amora"]

#para percorrer uma lista e exibir apenas seus eleentos,
#usamos for..im, como já vimos

for f in frutas:
    print(f)

print('_' *80)

#se quisermos percorrer a lista em ordem inversa para exibir
#apenas os elementos, usamos for..in combinado com reversed()

for a in reversed(frutas):
    print(a)

print('_' *80)

# agora, se precisamos exibir, além da informação sobre o elemento,
#também a sua posição, devemos usar range ()

for pos in range (len(frutas)):
    print(f"{pos}: {frutas[pos]}")

print('_' *80)

#percurso reverso usando range() com tres argumentos
for pos in range(len(frutas)-1, -1, -1):
    print(f"{pos}: {frutas[pos]} ")

