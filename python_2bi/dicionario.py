"""
um dicionario é uma estrutura de dados fornecida pela linguagem python,
capaz  de armazenar multiplos valores em uma única variável, por meio de pares de chave-valor.

"""

#um dicionário é delimitado por chaves{}
# as posições nomeadas de um dicionário são chamada PRORPRIEDADES


#diferença entre lista e dicionário em python:

#lista: delimitador = [] => ex lista[0]
#dicionário: delimitador = {} para acessar => decionario["posição"]

#lista: posições = numeradas
#dicionário: opsições = nomeadas

pessoa ={
    "nome": "Ozorimbo Oliveira Osório",
    "sexo": "M",
    "idade": 74,
    "peso": 76,
    "altura": 1.66
}

#acessando as variaveis armazenadas no dicionario

print("Nome:", pessoa["nome"])
print("Sexo:", pessoa["sexo"])
print("Idade:", {pessoa["idade"]})
print("Altura:", {pessoa["altura"]})

#calculando o IMC
IMC = pessoa['peso']/ pessoa['altura'] **2
print(f"O IMC de {pessoa['nome']} é {IMC}.")

####################################################################################################################

#representando formas geométricas planas por meio de dicionário

forma1 = {
    "base": 7.5,
    "altura": 12,
    "tipo": "R" #reângulo
}

forma2 = {
    "base": 6,
    "altura": 2.5,
    "tipo": "T" #triângulo
}

forma3 = {
    "base": 5,
    "altura": 3,
    "tipo": "E" #elipse
}

#função que calcula a área de uma forma deométrica plana
#sabendo as medidas sa base e da altura e o tipo de forma

from math import pi

def cal_area(forma):
    if forma["tipo"] == "R": #retângulo
        return forma["base"] * forma["altura"]
    elif forma["tipo"] == "T": # triângulo
        return (forma["base"]/2) * (forma["altura"]/2) *pi
    else: # forma desconhecida
        return None
    
print('-' *80)

print(f"Forma: {forma1['tipo']}; base: {forma1['base']}; altura: {forma1['altura']}; area: {cal_area(forma1)}")

print(f"Forma: {forma2['tipo']}; base: {forma2['base']}; altura: {forma2['altura']}; area: {cal_area(forma2)}")

print(f"Forma: {forma3['tipo']}; base: {forma3['base']}; altura: {forma3['altura']}; area: {cal_area(forma3)}")


# tipo de estruturas de dados

# 1- internas ou embutidas = geralmente, já são fornecidas pela propria linguagem e costuman
# ser genéricas, isto é, acertam quarquer tipo de dado exemplo em Python: listas e dicionarios

# 2- definidas pelo usuario = quando as estruturas internas de linguagem nao atendem as necessidades 
# da aplicação , pode-se criar estruturas personalizadas. Gerakmente essas estruturas sao baseadas 
# nos conceitos de classe e objeto

# classe força o objeto criado a partir dela a ter caracteristicas especificas,
# objeto é feito a partir da classe, mas força o objeto a ter defertmidas caracteristicas 
# a partir da classe.

# o objeto engloba: dados e algoritmos