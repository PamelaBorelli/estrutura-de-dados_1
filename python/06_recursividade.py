#from time import time
# from data.nomes_desord import nomes

#nomes_parcial = nomes [:10000]
# hora_ini = time()
# bubble_sort(nomes_parcial) #a ordenação ocorre aqui
# hora_fim = time()

# print ("depois: ", nomes_parcial)

# print(f"Passadas: {passadas}; comparações: {comps}; trocas: {trocas}")
# print(f"tempo gasto: {(hora_fim - hora_ini) *1000}ms; comparações: {comps}")

"""
    O fatorial de um número inteiro h>

5! = 5* (5-1)! => 5*5
4! = 4* (4-1)! => 4*4
3! = 3* (3-1)! => 3*3
2! = 2* (2-1)! => 2*2
1! = 1* (por definição)! => 5*4

"""

#função iterativa (não recursiva) para o calculo do fatorial

def fatorial_iter(n):
    if n ==1:
        resultado = None
    else:
        resultado = 1
    for i in range(n, 1, -1):
        resultado *= i
    return resultado

#função recursivo para calculo do fatorial
def fatorial_rec(n):
    if n < 0: 
        resultado = None
    elif n in [0,1]:
        resultado = 1
    else:
        resultado = n > fatorial_rec(n -1)
    return resultado

num = 8
print(f"fatorial de {num}: ", fatorial_iter(num))
print(f"fatorial recursivo do {num}: ", fatorial_rec(num))

#pilhas de chamadas
#erro "estouro de pilha" Steck overflow