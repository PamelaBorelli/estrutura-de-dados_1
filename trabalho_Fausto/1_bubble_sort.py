comps = trocas = passadas = 0

def bubble_sort(lista):

    global comps, passadas, trocas
    comps = trocas = passadas = 0

    # Loop eterno (não sabemos quantas passadas serão necessárias)
    while True:

        # Começa uma nova passada
        passadas += 1
        trocou = False

        # Percurso da lista, do primeiro ao último elemento
        # com acesso a cada posição

        # O loop só pode ir até a PENÚLTIMA posição
        for pos in range(len(lista) - 1):
            comps += 1
            if lista[pos + 1] < lista[pos]:
                # Efetua a troca
                lista[pos + 1], lista[pos] = lista[pos], lista[pos + 1]
                trocas += 1
                trocou = True

        if not trocou:  # Não houve troca na passada; ESTÁ ORDENADO!
            break   # Termina o loop eterno


# print("Antes:", empresas)
# bubble_sort(empresas)
# print("Depois:", empresas)
# print(f"Passadas: {passadas}; comparações: {comps}; trocas: {trocas}")

from time import time
from emp100mil import empresas
import tracemalloc



tracemalloc.start()
hora_ini = time()
bubble_sort(empresas)  # A ordenação ocorre aqui
hora_fim = time()
mem_atual, mem_pico = tracemalloc.get_traced_memory()

#print("Depois:", empresas)

print(f"Passadas: {passadas}; comparações: {comps}; trocas: {trocas}")
print(f"Pico de memória: { mem_pico / 1024 / 1024 } MB")
print(f"Tempo gasto: {(hora_fim - hora_ini) * 1000}ms; comparações: {comps}")

