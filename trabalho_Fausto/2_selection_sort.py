passadas = comps = trocas = 0

def selection_sort(lista):

    global passadas, comps, trocas
    passadas = comps = trocas = 0

    # Loop que vai da primeira até a PENÚLTIMA posição
    for pos_sel in range(len(lista) - 1):

        passadas += 1

        # Encontra o menor valor na sublista à frente de pos_sel
        pos_menor = pos_sel + 1
        for i in range(pos_sel + 2, len(lista)):
            comps += 1
            if lista[i] < lista[pos_menor]:
                pos_menor = i

        # Compara os elementos de pos_sel e pos_menor e faz a troca
        # se o valor do segundo for MENOR que o valor do primeiro
        comps += 1
        if lista[pos_menor] < lista[pos_sel]:
            # Efetua a troca
            lista[pos_sel], lista[pos_menor] = lista[pos_menor], lista[pos_sel]
            trocas += 1

from time import time
from emp100mil import empresas
import tracemalloc



tracemalloc.start()
hora_ini = time()
selection_sort(empresas)  # A ordenação ocorre aqui
hora_fim = time()
mem_atual, mem_pico = tracemalloc.get_traced_memory()

#print("Depois:", empresas)

print(f"Passadas: {passadas}; comparações: {comps}; trocas: {trocas}")
print(f"Pico de memória: { mem_pico / 1024 / 1024 } MB")
print(f"Tempo gasto: {(hora_fim - hora_ini) * 1000}ms; comparações: {comps}")