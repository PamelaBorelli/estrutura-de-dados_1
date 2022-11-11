import random
#importa uma "biblioteca" lista para o trabalho

import time
#importa uma biblioteca de tempo

def bubble_sort(v):
# define a função bubble_sort  
    fim = len(v)
# descobre onde termina o vetor, porque o fim vai diminuindo

    while fim > 0:

        i = 0
        # percorrendo o vetor de 0 até fim
        while i < fim -1: 
            if v[i] > v[i+1]:
                temp = v[i]
                v[i] = v[i+1]
                v[i+1] = temp
        # aqui houve a troca dos números maior para o menor
                #print(v)

            i +=1

        fim -= 1
        #diminui o tamanho do fim, ja que os números foram sendo ordenados

vetor = list(range(0,1000))
#cria um vetor ordenado automaticamente
random.shuffle(vetor)
#embaralha os dados d vetor criado


print(vetor)
antes = time.time() #antes da ordenação
bubble_sort (vetor)
depois = time.time() #depois da ordenação

total = (depois - antes) *1000 #conversão para ms
print("A ordenação demorou %0.2f ms" %total) 

print(vetor)


