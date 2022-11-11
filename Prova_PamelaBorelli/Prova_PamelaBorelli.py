"""
    1) Identifique o algoritmo abaixo.
    Quick sort
    2) Faça o mapeamento das variáveis (registre em comentário o propósito de cada uma delas).
    3) Há um erro no algoritmo. Identifique-o, descreva-o e corrija-o.
"""

def z(y, x = 0, w = None):
    #quando não soubermos o valor da variavel "fim"
    #vamos atribuir a ela a ultima posição da lista

    if w is None: w = len(y) - 1

    #para que o algoritimo trabalhe, é necessario que 
    # a faixa delimitada pelas variaveis "ini" e "fim"
    # tenha, pelo menos, dois elementos
    # caso contrario, saímos sem fazer nada

    if w <= x: return
    v = w
    u = x - 1

    #passadas +=1(? correção)

    #percorre a lista da posição "ini" até a posição "fim"
    for t in range(x, w):
        #compara os elementos das posições "pos" e "pivot"
        if y[t] < y[v]:
            w += 1 #u +=1 correção

             # incrementa a posição do divisor
        #se as variaveis "div" e "pos" forem diferentes entre 
        # si e o elemento de "pos" for menor que o elemento de "div"
        # promovea troca entre eles
            if t != u and y[t] < y[u]:
                y[t], y[u] = y[u], y[t]

    #depois que o loop acaba, o divisor é incrementado ainda uma vez
    w += 1 # u +=1 correção

#caso os valores de "div" e "pivot" sejam diferentes ente si,
# faz se a comparação ente os elementos da posição "div" e da 
# posição "pivot". caso este seja menor que aquele, promove-se a 
# troca ente eles
    if v != u and y[v] < y[w]: #if v! = u and y[v]< y [u] (correção)
        #trocas +=1 (correção)
        y[v], y[u] = y[u], y[v]
# o elemento na posição "div" está na posição correta agora

#chamamos recursivamente a função para ordenar a buslista a 
# esquerda da posição "div"
    z(y, x, u - 1)

# Fazemos o mesmo para ordenar a sublista à direita de "div".
    z(y, u + 1, w)