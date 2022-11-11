# ele é muito lento, ele eleva ao quadrado o tempo de ordenação, quanto ele
# está quase sorteado ele é mais rápido.

def sort(array):

    for final in range (len(array), 0, -1):
        exchanging = False
#vai da ultima posição do array até a posição "0", 
        print ("loop inicial") 

        for current in range(0, final -1):
#vai da posição "0 até a posição final -1"

            if array[current]> array[current +1]:
#compara o elemento atual com o próximo elemento      
                
                array[current], array[current +1] = array [current +1], array[current]
#troca o elemento atual recebe o proximo elemento, 
#e o proximo elemento recebe o elemento atual
                exchanging = True
        
        if not exchanging:
            break


array = sorted ([8,7,5,3,1,2,9,6,4])
sort(array)
print (array)
