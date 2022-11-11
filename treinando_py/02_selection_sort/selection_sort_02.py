def selection_sort(lista):
    n = len(lista) #serve para contrair a escrita
    for j in range(n-1): #variavel que vai correr a lista a partir da posição "0"
        min_index = j# procura o número menor da lista começando da posição "0"
        for i in range(j, n): #corre a lista
            if lista[i]< lista[min_index]: #procura o menor valor da lista
                min_index = i # coloca o menor valor em evidência
    
    
        if lista[i] > lista[min_index]: #agora vai comparar o número selecionado na posição "0"com os outros da lista
            aux = lista[j] #variavel auxiliar para a próxima função
            lista[j] = lista[min_index] #coloca o número na posição "0" no lufgar da mínimo
            lista[min_index] = aux #agora coloca o mínimo na posição "0"


lista = [7,5,1,8,3]
print ("Lista ainda não ordenada: ", lista)
selection_sort(lista)
print("Lista já ordenada: ", lista)
