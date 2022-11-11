divs = comps = juncs = 0

def merge_sort(lista):

    global divs, comps, juncs

    # Só continua dividindo se o tamanho da lista
    # for maior que 1
    if len(lista) <= 1: return lista

    # Encontra a posição (inteira) do meio da lista
    meio = len(lista) // 2

    # Tira uma cópia da primeira metade da lsita
    sublista_esq = lista[:meio]
    # Tira uma cópia da segunda metade da lista
    sublista_dir = lista[meio:]
    divs += 1   # Contabiliza uma divisão

    # Chamamos recursivamente a função para que ela
    # continue repartindo cada uma das sublistas em
    # metades
    sublista_esq = merge_sort(sublista_esq)
    sublista_dir = merge_sort(sublista_dir)

    # AQUI COMEÇA A MESCLAGEM ORDENADA DAS DUAS
    # METADES DA LISTA

    # Inicialização das "setas"
    pos_esq = pos_dir = 0
    ordenada = []       # Lista vazia

    # Compara os elementos das sublistas entre si e
    # insere na lista ordenada o que for menor
    while pos_esq < len(sublista_esq) and pos_dir < len(sublista_dir):
        comps += 1
        # O menor elemento está na sublista da esquerda
        if sublista_esq[pos_esq] < sublista_dir[pos_dir]:
            # "Desce" o elemento da esquerda para a lista ordenada
            ordenada.append(sublista_esq[pos_esq])
            # Incrementa pos_esq
            pos_esq += 1
        # O menor elemento está na sublista da direita
        else:
            # "Desce" o elemento da direita para a lista ordenada
            ordenada.append(sublista_dir[pos_dir])
            # Incrementa pos_dir
            pos_dir += 1

    # Verificação da sobra
    sobra = []  # Lista vazia

    # Sobra à esquerda
    if(pos_esq < pos_dir): sobra = sublista_esq[pos_esq:]
    # Sobra à direita
    else: sobra = sublista_dir[pos_dir:]

    # Contabiliza uma junção
    juncs += 1

    # O resultado final é a concatenação (junção) da lista
    # ordenada com a sobra
    return ordenada + sobra

from time import time
from emp10mil import empresas
import tracemalloc

divs = comps = juncs = 0

tracemalloc.start()     # Inicia o monitoramento da memória
hora_ini = time()
emp100mil = merge_sort(empresas)  # A ordenação ocorre aqui
hora_fim = time()
mem_atual, mem_pico = tracemalloc.get_traced_memory()

# Exibe só os 1000 primeiros, para andar mais rápido
#print("Depois:", nomes_ord[:1000]) 

print(f"Tempo gasto: {(hora_fim - hora_ini) * 1000}ms")
print(f"Pico de memória: { mem_pico / 1024 / 1024 } MB")
print(f"Divisões: {divs}; comparações: {comps}; junções: {juncs}")
