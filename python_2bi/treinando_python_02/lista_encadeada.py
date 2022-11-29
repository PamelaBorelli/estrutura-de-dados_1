'''
lista encadeada 

'''

class Node:
    def __init__ (self, data):
        self.data = data
        self.next = None

#import node import Node 

class LinkedList:
    def __init__(self): 
        self.head = None # a lista começa vazia
        self._size = 0

    def append(self, elem): # elem colocado no fim da lista
        if self.head: # inserindo o 1º elem na lista
            pointer = self.head #ponteiro para quando a lista já tem elemento
            while(pointer.next):
                pointer = pointer.next # percorre a estrutura para encontrar o ultimo elemento
                pointer.next = Node(elem) #colcoca o elemento no ultimo espaço (ainda vazio)
        else:
            self.head = Node (elem) #primeira inserção
        self._size = self._size +1
    
    def __len__(self):
        return self._size # retorna o tamanho da lista

    def get(self, index):
        pass

    def set(self, index, elem):
        pass

    def __getitem__ (self, index): # sobrecarga de operador
        pointer = self.head
        for i in range(index):
            if pointer:
                pointer = pointer.next
            else: 
                raise IndexError("List index out of range")

        if pointer: 
            return pointer.data
        raise IndexError("List index out of range")

    def __setitem__(self, index, elem):
        pointer = self.head
        for i in range(index):
            if pointer:
                pointer = pointer.next
            else: 
                raise IndexError("List index out of range")

        if pointer: 
            pointer.data = elem # novo elem
        else:
            raise IndexError("List index out of range")

    def index (self, elem):
        '''Retorna o indice do ekem na lista'''
        pointer = self.head
        while(pointer):
            if pointer.data ==elem:
                return i
            pointer = pointer.next
            i = i+1

        raise ValueError ("{} is not in list", format(elem))



lista = LinkedList()
lista.append(7)

print(lista)
