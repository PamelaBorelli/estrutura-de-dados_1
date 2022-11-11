"""
    1) Identifique o algoritmo abaixo.
    Selection sort
    2) Faça o mapeamento das variáveis (registre em comentário o propósito de cada uma delas).
    3) Há um erro no algoritmo. Identifique-o, descreva-o e corrija-o.
"""

def z(y):
    for x in range(len(y) - 1): 
    #seleciona o número atual


        w = x + 1 
        #pega o numero menor e coloca temporariamente como numero menor
        
        for i in range(x + 2, len(y)):
        #seleciona o número a direita para ser comparado com da esquerda


            if y[i] < y[x]: #ify[i}<y[w] (correção)
            #condição para comparar (se acontece isso)

                w = i 
                #consição para comparar (acontece isso)
        
        #compara os elementos de pos_sel e pos_ menor e faz a troca
        #se o valor do segundo form menor que o valor do primeiro
        if y[w] < y[x]:
            #w = i (correção)
            y[x], y[w] = y[w], y[x]
            #trocas +=1
            #aqui realmente realiza a troca