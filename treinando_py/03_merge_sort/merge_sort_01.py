#dividir e conquistar (divide a lista e trabalha com porções pequenas)
#ele é um algoritmo mais rápido, porém ele é mais complexo para escrever
#já comecei o video 2


from tracemalloc import start


def sort(array):
    aux = array[:] #variavel que guarda o numero enquanto o array é divido
    sort_half(array, aux, 0, len(array) -1)#começa da primeira posição até a ultim


def sort_half(array, aux, inicio, fim):
    if inicio >= fim: 
        return
    
    meio = (inicio + fim) //2 #essa é a função que divide o array no meio
    
    sort_half(array, aux, inicio, meio)# a partir daqui divide o array no meio
    sort_half(array, aux, meio +1, fim)

    merge(array, aux, inicio, fim)

def merge (array, aux, inicio, fim):#faz a troca dos elementos no pedaço que foi dividido
    #array[inicio: fim + 1] = sorted (array[inicio:fim +1]) // essa parte é so um atalho para mostrar que ele funciona
    #pass#é a função pirncipal para troca dos elementos
    esquerdo = inicio
    esquerdoFim = (inicio + fim) //2 

    direito = esquerdoFim + 1
    direitoFim = fim

    posicao = inicio

    for posicao in range (inicio, fim +1):
    # while esquerdo <= esquerdoFim or direito <= direitoFim: (essa função não é boa)
        # aqui vai analisando elementos do esquerdo 1ª e direito 2º
        if esquerdo > esquerdoFim:
            aux[posicao] = array[direito]
            direito +=1
            #posicao +=1 com a função "for" não precisa encrementar a posição

        #aqui analisa os elementos da direita
        elif direito > direitoFim:
            aux[posicao] = array[esquerdo]
            esquerdo +=1
            #posicao +=1 com a função "for" não precisa encrementar a posição

        #aqui compara esquerdo com direito
        elif array [esquerdo] < array[direito]:
            aux[posicao] = array[esquerdo]
            esquerdo +=1
            #posicao+=1 com a função "for" não precisa encrementar a posição


        else:
            aux[posicao] = array[direito]
            direito +=1
            # posicao +=1 com a função "for" não precisa encrementar a posição

    for k in range(inicio, fim +1):
        #função com os numeros já em ordem
        array[k] = aux [k]

array = [9,8,7,5,6,3,1,2]
copy_array = array [:]

sort(array)
print(array)

assert array == sorted (copy_array)