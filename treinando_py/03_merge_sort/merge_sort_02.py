import random
#importa uma "biblioteca" lista para o trabalho

import time
#importa uma biblioteca de tempo

def merge_sort (lista, inicio=0, fim=None):
    if fim is None:
        fim = len(lista)

    if (fim - inicio > 1):
        meio = (fim + inicio)//2
        merge_sort (lista, inicio, meio) 
        merge_sort(lista, meio, fim)
        merge(lista, inicio, meio, fim)

def merge (lista, inicio, meio, fim):
    esquerda = lista [inicio:meio]
    direita = lista [meio:fim]

    i, j = 0, 0
    for k in range (inicio, fim):
        if i >= len(esquerda): 
            lista[k] = direita[j]
            j = j +1 

        if j >= len(direita):
            lista[k] = esquerda[i]
            i = i + 1

        if esquerda[i] < direita [j]:
            lista[k] = esquerda[i]
            i = i + 1
        else:
            lista[k] = direita [j] 
            j = j +1


lista = list(range(0,1000))
#cria um vetor ordenado automaticamente
random.shuffle(lista)
#embaralha os dados d vetor criado


print(lista)
antes = time.time() #antes da ordenação
merge_sort (lista)
depois = time.time() #depois da ordenação

total = (depois - antes) *1000 #conversão para ms
print("A ordenação demorou %0.2f ms" %total) 

print(lista)