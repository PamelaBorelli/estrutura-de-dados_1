'''
    Algoritmo de ordenação merge sort

    no cprocesso de ordenação, pesse algoritmo "desmonta" o valor original 
    contendo N elementos até obter N valores com apenas um elemento cda um. 
    Em seguida, usando a tecnica de mesclagem (merge), remonta o vetor, dessa 
    vez com os elementos em ordem.
'''

def merge_sort(lista):
    # só continua dividindo se o tamnanho da lista for maior que 1
    if len(lista) <=1: return lista
    #encontra a posição (inteiro) do meio da lista
    meio = len(lista) // 2
    # tira uma copia da primeira metade da lista
    sublista_esq =lista[:meio]
    #tira uma copia da segunda metade da lista
    sublista_dir = lista[meio:]

    # chamamos recursivamente a função para que ela
    #continue repartindo cada uma das sublistas em metades

    sublista_esq = merge_sort(sublista_esq)
    sublista_dir = merge_sort(sublista_dir)

    # aqui começa a mesclagem ordenada das duas metades da lista
    #iniciação das "setas"

    pos_esq = pos_dir = 0
    ordenada = [] #lista vazia

    #compara os elementos das sublistas entre si e insere na 
    # lista ordenada o que for menos
    while pos_esq < len (sublista_esq) and pos_dir < len (sublista_dir):
        #o menor elemento esra na sublista da esquerda
        if sublista_esq[pos_esq] < sublista_dir[pos_dir]:
            #"desce" o elemetento da esquerda paa a lista ordenada
            ordenada.append(sublista_esq[pos_esq]) 
            # incrementa pos_esq
            pos_esq +=1
        # o menor elementoesta na lista da direita
        else:
            ordenada.append(sublista_dir[pos_dir])
            #incremento pos_dir
            pos_dir +=1

    # verificação da sobra
    sobra = [] #lista vazia

    #sobra a esquerda
    if(pos_esq < pos_dir): sobra = sublista_esq[pos_esq:] 
    #sobra o direito
    else: sobra = sublista_dir[pos_dir:]

    # o resultado final é a concaternação (junção) da lista ordenada com a sobra
    return ordenada + sobra

#################################################################################

# nums = [7, 3, 6, 8, 1, 4, 9, 0, 5, 2]

# nums_ord = merge_sort(nums)

# print("Lista original: ", nums)
# print("Lista ordenada: ", nums_ord)
# print("divisões: {divs}: comparações: {comps}: junções: {juncs}")

###############################################################################

from time import time
import tracemalloc
from data.nomes_desord import nomes

divs = comps = juncs = 0

tracemalloc.start ()
hora_ini = time()
nomes_ord = merge_sort(nomes)  # A ordenação ocorre aqui
hora_fim = time()
mem_atual, mem_pico =tracemalloc.get_traced_memory()

print("Depois:", nomes_ord[:1000])
print(f"Tempo gasto: {(hora_fim - hora_ini) * 1000}ms")
print(f"pico de memória: {mem_pico/ 1024/ 1024} MB")
print(f"divisões: {divs}: comparações: {comps}: junções: {juncs}")



