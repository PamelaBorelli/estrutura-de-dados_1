#serve para uma lista não ordenada

def busca (lista, elem):
    """Retorna o indice elem se ele estiver na lista ou None, caso contrario"""
    for i in range(len(lista)):
        if lista[i] ==elem:
            return i
    return None

lista_estranha = [8, "5", 32, 0, "Python", 11]
elemento= 8

indice = busca(lista_estranha, elemento)
if indice is not None:
    print("o indice do elemento {} é {}".format(elemento, indice))
else:
    print("o elemento {} não se encontra na lista".format(elemento, indice))