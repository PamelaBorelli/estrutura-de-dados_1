# a lista tem que estar ordenada, pode-se usar bubble, selection, merge sort 
# primeiro para depois fazer a busca binaria

def buscaBinaria(array, item, comeco=0, fim=None):
    if fim is None:
        fim = len(array)-1
    # aqui divide o array no meio e encontra o número do meio
    meio = (comeco + fim)//2
    if array[meio] ==item:
        return meio
    
    #se o elemento for menor que o meio,
    #pego o meio e comparo os elementos da esquerda(lembrando meio -1)
    if item < array[meio]:
        return buscaBinaria(array, item, comeco, meio-1)
    else:
    #se o elemento for maior que o meio, comparo o meio até o fim
        return buscaBinaria(array, item, meio +1, fim)
    return None


# lista=[1,2,3,4,5,6,7,8,9]
# buscaBinaria(lista, 4)

import random
from teste import buscaBinaria
