#variaveis de estatistivas
passadas = comps = trocas = 0


def quick_sort(lista, ini = 0, fim = None):
    #quando não soubermos o valor da variavel "fim"
    #vamos atribuir a ela a ultima posição da lista

    if fim is None: fim = len(lista) -1

    #para que o algoritimo trabalhe, é necessario que 
    # a faixa delimitada pelas variaveis "ini" e "fim"
    # tenha, pelo menos, dois elementos
    # caso contrario, saímos sem fazer nada

    if fim <= ini: return
    
    global passadas, comps, trocas
    # inocialização das variaveis

    pivot = fim
    div = ini -1
    passadas +=1

    #percorre a lista da posição "ini" até a posição "fim"
    for pos in range (ini,fim):
        comps +=1
        #compara os elementos das posições "pos" e "pivot"
        if lista[pos] < lista[pivot]:
            div +=1 # incrementa a posição do divisor
        #se as variaveis "div" e "pos" forem diferentes entre 
        # si e o elemento de "pos" for menor que o elemento de "div"
        # promovea troca entre eles
            comps +=1
            if pos != div and lista[pos] < lista[div]:
                lista [pos], lista[div] = lista[div], lista[pos]#troca

#depois que o loop acaba, o divisor é incrementado ainda uma vez
    div += 1 

#caso os valores de "div" e "pivot" sejam diferentes ente si,
# faz se a comparação ente os elementos da posição "div" e da 
# posição "pivot". caso este seja menor que aquele, promove-se a 
# troca ente eles
    comps +=1
    if pivot != div and lista[pivot] < lista[div]:
        trocas +=1
        lista[pivot], lista[div] = lista[div], lista[pivot]#troca

# o elemento na posição "div" está na posição correta agora

#chamamos recursivamente a função para ordenar a buslista a 
# esquerda da posição "div"
    quick_sort(lista, ini, div - 1)

# Fazemos o mesmo para ordenar a sublista à direita de "div".
    quick_sort(lista, div + 1, fim)
    
####################################################################################

# nums = [7, 3, 6, 8, 1, 4, 9, 0, 5, 2]

# passadas = comps = trocas = 0
# print("Antes:", nums)
# quick_sort(nums)
# print("Depois:", nums)
# print(f"Passadas: {passadas}; comparações: {comps}; trocas: {trocas}")

#################################################################################

from time import time
from data.nomes_desord import nomes
import tracemalloc

passadas = comps = trocas = 0

tracemalloc.start()     # Inicia o monitoramento da memória
hora_ini = time()
quick_sort(nomes)  # A ordenação ocorre aqui
hora_fim = time()
mem_atual, mem_pico = tracemalloc.get_traced_memory()

# Exibe só os 1000 primeiros, para andar mais rápido
print("Depois:", nomes[:1000]) 

print(f"Tempo gasto: {(hora_fim - hora_ini) * 1000}ms")
print(f"Pico de memória: { mem_pico / 1024 / 1024 } MB")
print(f"Passadas: {passadas}; comparações: {comps}; trocas: {trocas}")