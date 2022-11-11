#listas em python
#listas são uma forma de ormazenar mais de um valor
# em uma única variável. Os valores poder ser de tipos diferentes

valores = [2,3,5,7,9,11,13,17,19, "batata", "cenoura", True]

#operações sobre listas

#1) percurso: significa percorrer a lista do primeiro até o ultimo,
#fazendo algo com cada um deles. No caso, vamos exibir cada um dos elementos com print()

for v in valores:
    print(v)

#2) inserção de um novo elemento no final da lista: append()
valores.append("cebola")
print(valores)
valores.append(29)
print(valores)

print('_' *80)

#3) inserindo um novo elemento em uma posição especificada: insert()
#parametros:
#1º posição para inserir 
#2º valor a ser inserido

valores.insert(4,"chuchu") #inserindo "chuchu" na quarta posição
print(valores)

#inserindo "abrobrinha na primeira posição"
valores.insert(0,"abrobrinha")
print(valores)

print ('_' *80)

#$) acessando um valor em uma posição específica
# impremindo o setimo valor da lista
print(valores[6])
#impremindo o terceiro valor da lista
print(valores[2])
#impremindo o primeiro valor da lista
print(valores[0])
#impremindo o ultimo valor da lista 
print(valores[-1])
#imprimindo o penultimo valor dal ista 
print(valores[-2])

print('_' *80)

#5) substituindo valores existenres na lista

print('Antes:', valores)
#subistituindo o valor da posição 10(11ª elemento)
valores[10] = "tomate"
#substituindo o valor da posição 0 (1ªelemento)
valores[0] = 'beterraba'
#subustituindo o valor da ultima posição
valores[-1] = "mandioca"
print("depois", valores)

print('_' *80)

#6) deterninando quantos elementos ha na lista: len()
print("número de elementos na lista", len(valores))
#imprimindo o ultimo elemento da lista com a ajuda do len()
print("ultimo elemento: ", valores[len(valores)-1])

print('_' *80)
#7) removendo o ultimo elemento da lista: pop()
print("antes:", valores)
ultimo = valores.pop()
print(f"valor removido da lista: {ultimo}")
print("depois: ", valores)

print('_' *80)

#8) removendo um elemento por sua posição: pop() com paramentros
print("antes:", valores)
pos12 = valores.pop(12)
print(f"valor removido da posição 12: {pos12}")
pos0 = valores.pop(0)
print(f"valor removido da posição : {pos0}")
print("depois: ", valores)

print('_' *80)

# 9) removendo um elemento por seu valor: remove()
print("antes: " , valores)
valores.remove("chuchu") # remove o valor "chuchu"
valores.remove(11)       # remove o valor 11
print("depois: ", valores)   

print('_' *80)
# 10) faltiando uma lista

# Cria uma sublista que contem os elementos da posição 0
#até a posiclçao 6 (posição 7 não entra)
sublista0_6 = valores[0:7]
print("sublista0_6", sublista0_6)

#cria uma sublista que contém os elementos da posição 4
#até a posição 9 (posição 10 não entra)
sublista4_9 = valores[4:10]
print("sublista4_9", sublista4_9)

#cria uma sublista que contem os elementos do inicio 
# ate a posição 7(posição 8 nao entra)
sublista0_7 = valores[:8]
print("sublista0_7", sublista0_7)

#cria uma sublista que contém os elementod a partir da
#posição 6 até a final
sublista6fim = valores[6:]
print("sublista6_fim", sublista6fim)



