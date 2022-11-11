def selection_sort (array):
    for num_atual in range(0, len(array)): 
        #seleciona o número atual
        num_menor = num_atual 
        #pega o numero menor e coloca temporariamente como numero menor

        for num_direita in range (num_atual +1, len(array)): 
            #seleciona o número a direita para ser comparado com da esquerda
            if array [num_direita] < array [num_menor]: 
                #condição para comparar (se acontece isso)
                num_menor = num_direita                 
                #consição para comparar (acontece isso)
        array[num_atual], array[num_menor] = array[num_menor], array[num_atual] 
        #aqui realmente realiza a troca

array = [9,8,7,6,5,4,3,2,1]
selection_sort (array)
print ("Lista ordenada: ", array)