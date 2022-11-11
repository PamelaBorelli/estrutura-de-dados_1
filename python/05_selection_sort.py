"""
Algoritmo sw ordenação selection sort

Isola (seleciona) o primeiro elemento da lista e, em seguida,
encontra o menor valor no restante da lista. Se o valor encontrado 
for menor que o valor previamente selevionado, efetua a troca.
Continuando, seleciona o segundo elemento da lista, buscando pelo
menoe valor das posições subsequentes. Faz a trova entre os dois valores,
se necessárop. O processo se repere até que o ultimo elemento da lista 
seja isolado, comparando com o ultimo e feita a troca entre eles,
se pertimente.
"""
passadas = comps = trocas = 0
def selection_sort(lista):

    global passadas, comps, trocas
    passadas = comps = trocas = 0

    #Loop que vai da primeira até a penultima posição
    for pos_sel in range (len(lista) -1):

        passadas +=1

        #encontra o menor valor, na sublista a frente de pos_sel
        pos_menor = pos_sel +1
        for i in range(pos_sel + 2, len(lista)):
            comps +=1
            if lista[i] < lista[pos_menor]:
                pos_menor = i

        #compara os elementos de pos_sel e pos_ menor e faz a troca
        #se o valor do segundo form menor que o valor do primeiro
        comps +=1
        if lista[pos_menor] < lista[pos_sel]:
            #efetua a troca
            lista[pos_sel], lista[pos_menor] = lista[pos_menor], lista[pos_sel]
            trocas +=1

#nums = [7, 3, 6, 8, 1, 4, 9, 0, 5, 2]

# Pior caso
#nums = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]

#melhor caso
# nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# print("Antes: ", nums)
# selection_sort(nums)
# print("Depois: ", nums)
# print(f"Passadas: {passadas}; comparações: {comps}; trocas: {trocas}")

################################################################################

from time import time
import tracemalloc
from data.nomes_desord import nomes


tracemalloc.start ()
hora_ini = time()
nomes_ord = selection_sort(nomes)  # A ordenação ocorre aqui
hora_fim = time()
mem_atual, mem_pico =tracemalloc.get_traced_memory()

print("Depois:", nomes[:1000])

print(f"Tempo gasto: {(hora_fim - hora_ini) * 1000}ms; comparações: {comps}:")
print(f"pico de memória: {mem_pico/ 1024/ 1024} MB")
print(f"passadas: {passadas}: comparações: {comps}: trocas: {trocas}")