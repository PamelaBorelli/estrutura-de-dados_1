"""
    1) Identifique o algoritmo abaixo.
    busca binaria
    2) Faça o mapeamento das variáveis (registre em comentário o propósito de cada uma delas).
    3) Há um erro no algoritmo. Identifique-o, descreva-o e corrija-o.
"""    

def z(y, x):
    w = 0
    v = len(y) - 1
    while w <= v:
    # Encontra o meio da lista
        u = (w + v) // 2

        # 1º caso: o valor na posição do meio da lista
        # corresponde ao valor buscado; ENCONTRAMOS e
        # retornamos a posição encontrada (meio)
        if x == y[u]: v = u #v=u (excluir)
        #return meio (correção)

        #2º caso: o valor de busca é menor que o valor no meio da lista
        elif x < y[u]: v = u - 1

        #3º caso: o valor de busca é maios que o valor que no meio da lista
        else: w = u + 1
    return -1 #valor de busca não existe