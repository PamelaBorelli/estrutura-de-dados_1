nums =[9, 21, 33, 12, 0, 18, 24, 30, 15, 6, 3, 27]

'''
função que realiza uma busca sequencial em uma lista procurando val, 
se val for encontrado, retorna a posicção de val,
se val não for encontrao, retorna o valor -1

'''
def busca_sequencial(lista, val):
    for pos in range(len(lista)):
        #encontrou val: retorna a posição onde foi encontrado
        if val == lista[pos]: return pos
    #percorreu todo a lista e não encontrou val: retorna -1
    return -1

#testes
# procurando o número 15
resultado = busca_sequencial(nums, 15)
print (f"Posição do valor 15 na lista: {resultado}")

resultado = busca_sequencial(nums, 20)
print (f"Posição do valor 20 na lista: {resultado}")

resultado = busca_sequencial(nums, 33)
print (f"Posição do valor 33 na lista: {resultado}")



