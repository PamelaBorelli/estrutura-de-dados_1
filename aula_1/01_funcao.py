def imc(peso, altura):
    resultado = peso/altura ** 2
    return resultado

# p =float (input("irforme o peso: "))
# a =float (input("Informe a altura: "))

# i = imc(p,a) #chamada à função

# print(f"O IMC calculado é {i:.2f}") #2 casas decimais

##############################################################
from math import pi 

"""
Função que calcula uma área de uma figura geométrica de acordo com o tipo especificado
"""
def calc_area(base, altura, tipo):
    if tipo == "R": 
        area = base*altura
    elif tipo == "T":
        area = base*altura/2
    elif tipo == "E":
        area = (base/2) * (altura/2) * pi 

    else: 
        area = None 

    return area

print(f"Retângulo  10x25: {calc_area(10,25,'R')}")
print(f"Área triângulo 15x25: {calc_area(15, 12, 'T')}")
print(f"Área elipse 20x25: {calc_area(20, 25, 'E')}")
print(f"Área ??? 7x5.5: {calc_area(7, 5.5, 'W')}")




