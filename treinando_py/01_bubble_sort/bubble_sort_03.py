#precisa importar uma lista "_pycache_"

def bubble_sort (lista):
    n = len(lista)
    for j in range(n-1): #fim e repetição

        for i in range(n -1):
            if lista[i] > lista[i+1]:
                lista[i], lista [i+1] = lista[i+1], lista[i]

