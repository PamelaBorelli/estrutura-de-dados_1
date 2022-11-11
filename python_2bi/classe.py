# classe é um estrutura que representa conjuntamente dados e algotmos.
# uma classe pode ser comparada a uma "assadeira" com q auqal se pode fazer diferentes 
# "assados" (objetos), variando as "ingredientea" (dados) e o "modo de fazer" (algoritmo).
# apesar dessa variação, todos os onjetos creiados a partir da mesma classe terao 
# sempre o formato determinado por este.


import os

from math import pi

class FormaGeometrica:

    # uma classe pode ter, dentro de si, tanto dados quanto funções 
    # (estas representando os algoritmos). Uma função especial, chamada __init__,
    # é chamada sempre que um novo objeto é criado a partir de uma classes.
    # essa função especial é chamada de CONSTRUTOR.

    # quando aparecem dentro de um classe:
    # --> funções passam a ser chamadas de MÉTODOS, e seu primeiro parametro
    # é sempre chamado self, representando a propria objeto
    # --> variaveis passam a ser chamadas de ATRIBUTOS

    def __init__ (self, base, altura, tipo):
        #validando o valor da base
        

        # validando o valor da altura
            

        # validando o tipo
        


        #armazenando os dados recebidos dentro do objeto
        self.__base = base
        self.__altura = altura
        #self.set__altura(altura)
        self.__tipo = tipo

    #metodo setter para o atributo __base
    def set__base(self, val):
        if type(val) not in [int, float] or val <=0:
            raise Exception(f"ERRO: a base ({val}) deve ser númerica e maior que zero")
        self.__base == val

    #método setter oara o atributo __tipo
    def set__tipo(self, val):
        if val not in ["R", "T", "E"]:
            raise Exception(f"ERRO: o tipo ({val}) deve ser R, T, E")
        self.__tipo == val

    #método setter para o atributo __altura 
    def set__altura(self, val):
        if type(val) not in [int, float] or val <=0:
            raise Exception(f"ERRO: a altura ({val}) deve ser númerica e maior que zero")   
        self.__altura == val
        
    #método getter para o atributo __altura
    def get__altura(self):
        self.__altura

    #método getter para o atributo __base
    def get__base(self):
        self.__base

    #método getter para o atributo __tipo
    def get__tipo(self):
        self.__tipo

    #metodo que gera uma reepresentaação da forma geometrica
    def cal_area(self):
        if(self.__tipo =="R"):
            return self.__base * self.__altura
        if(self.__tipo =="T"):
            return self.__base * self.__altura / 2
        if(self.__tipo =="E"):
            return (self.__base / 2) * (self.__altura / 2) * pi

    #método que gera uma representação de um objeto como string
    def __str__(self):
        return f"base = {self.__base}, altura = {self.__altura}, tipo = {self.__tipo}"

######################################################################################################

#criando tres objetos a partir da classe:

forma1 = FormaGeometrica(20, 15, 'R')
forma2 = FormaGeometrica(1.5, 3.5, 'T')
forma3 = FormaGeometrica(4, 4.2, 'E')
# forma4 = FormaGeometrica(-3, "tomate", 'Z')

#forma1.set__altura = -7

print(f"forma1: {forma1}")
print(f"forma2: {forma2}")
print(f"forma3: {forma3}")
# print(f"forma3: {forma4.template}")

forma1.set__altura(9)

print('Altura atualizada de forma1: ', forma1.get__altura())

print('forma1 atualizada: ', forma1)

print(f'forma1: {forma1}, area -> {forma1.cal_area()}')
print(f'forma2: {forma2}, area -> {forma2.cal_area()}')
print(f'forma3: {forma3}, area -> {forma3.cal_area()}')

# Atributos publicos
# pode ter seu valor modificado, tanto dentro como fora da classe



# Atributos privados
# so pode ser modificado dentro da classe
# os nomes dos atributos começam com dois "_ _" 

# Getter => método público que dá acesso a atributos privados
# Setter => método público que permite modificar de forma controlada os
#           atributos privados


# objeto é uma associoação de dados com algoritmos, criados a partir de um modelo: a classe

# estrutura de dados é uma forma particular de organização dos dados
# de forma a otimizar a o desenvolvimento e a execução de algoritimos que utilizam
# esses dados.
# em geral, cada estrutura de dados resolve u problema específico

# Pilha: resolve o problema da inversão 
# ex: [1, 2, 3, 4, 5] => [5, 4, 3, 2, 1]
    # 5 
    # 4
    # 3
    # 2
    # 1

# regra de LIFO => o ultimo a entrar é o primeiro a sair

# append => insere um elemento na ultima posição
# insert => insere um elemento em qualquer posição
# pop => remove e devolve o ultimo elemento da lista



# Fila, Deque, Lista duplamente encadeada, Grafo, Árvore Binária de busca