#LISTA DUPLAMENTE ENCADEADA

'''
    Classe que representa uma unidade de informação na lista duplamente encadeada
'''

class Node:

    """ Método Construtor """

    def __init__(self, data):

        self.prev = None    #Ponteiro para o nodo anterior
        self.data = data    #Dado do usuário
        self.next = None    #ponteiro para o nodo seguinte

"""
    ESTRUTURA DE DADOS LISTA DUPLAMENTE ENCADEADA

    trata-se de uma lista linear, em que seus elmentos (nodos)
    não estão adjacentes fisicamente uns dos outros, mas ligados
    logicamente por meio de ponteiros que indicam o nodo anterior
    e o próximo nodo da sequÊncia. Não tem restrição de acesso -
    inserções, exclusões e consultas podem ser realizadas em qualquer
    posição da lista.
"""

class DoublyLinkedList: 

    """ Método Construtor """

    def __init__(self):
        self.__head = None # Ponteiro para o primeiro nodo
        self.__tail = None # POnteiro parao último nodo
        self.__count = 0   # Quantidade de nodos 

    """ Método que retorna se a lista está vazia ou não"""

    def is_empty(self):
        return self.__count == 0

    """
        Método que encontra e retorna o nodo da posição especificada
    """

    def __find_node (self, pos):
        # 1º caso: posição 0, retorna __head
        if pos == 0: return self.__head

        # 2º caso: posição final (self.__count - 1)
        if pos == self.__count - 1: return self.__tail

        # 3º caso: nodo em posição intermediária

        # Se a posição estiver na primeira metade da lista,
        # faz o percurso a partir do __head, seguindo next
        elif pos < self.__count//2:

            # Percorre a lista quantas vezes for necessário
            # para encontrar o nodo
            node = self.__head # começa pelo primeiro nodo
            for i in range (1, pos +1): node = node.next
            return node
        # Senão, a posição estando na seunda metade da lista,
        # faz o percurso reverso a partir de __tail, seguindo
        #prev
        else:
            node = self.__tail # começa pelo último nodo
            for i in range (self.__count -2, pos - 1, -1):
                node = node.prev


    """" Método que insere um novo valor à lista """

    def insert(self, pos, val):

        #criamos um novo nodo que armazena a informação do usuário e 
        #também os ponteiros prev e next. Ambos apontando para None

        inserted = Node(val)

        # 1º caso: a lista está vazia e este é primeiro nodo
        # a ser inserido

        if (self.is_empty):
            self.__head = inserted
            self.__tail = inserted

        # 2º caso: inserção no início da lista (posição 0)
        elif pos == 0:
            inserted.next = self.__head
            self.__head.prev = inserted
            self.__head = inserted

        # 3º caso: inserção na posição final
        # Obs.: consideramos como posição final qualquer valor
        # que seja >= self.__count
        elif pos >= self.__count:
            inserted.prev = self.__tail
            self.__tail = inserted

        # 4º caso: inserção em posição intermediária
        elif pos > 0:
            pass # não faz nada

        # Incrementa a contagem de nodos
        self.__count += 1

        