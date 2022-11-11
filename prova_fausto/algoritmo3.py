"""
    1) Identifique o algoritmo abaixo.
    2) Faça o mapeamento das variáveis (registre em comentário o propósito de cada uma delas).
    3) Há um erro no algoritmo. Identifique-o, descreva-o e corrija-o.
"""

def a(b):
    while True:
        c = False
        for d in range(len(b) - 1):
            if b[d + 1] < b[d]:
                b[d + 1], b[c] = b[c], b[d + 1]
                c = True
        if not c:
            break

lista_estranha = [8, "5", 32, 0, "Python", 11]
elemento= 50

indice = a(lista_estranha, elemento)
if indice is not None:
    print("o indice do elemento {} é {}".format(elemento, indice))
else:
    print("o elemento {} não se encontra na lista".format(elemento, indice))