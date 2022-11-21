# dados enfilerados, diferente da pilha o primeiro elemento que entrou o primeiro que sai

# push== é colocado atras da pilha
# pop == exlui o primeiro elemento da pilha
# empty ==  false pq a fila nao está vazia
# top ou peek = retorna o elemento que é o proximo
# size == tamanho

# QUEUE = elementos == size , first, last 
#node == elemento (data, next)

class Node:
    def __init__(self, data) :
        self.data = data
        self.next = None

class Queue:
    def __init__(self):
        self.first = None
        self.last = None
        self._size = 0


    def push(self, elem):
        node = Node(elem)

        if self.empty():
            self.last = node

        else:
            self.last.next = node
            self. last = node

        if self.first is None: # outra forma de escrever o if de cima
            self.first = node
        self._size += 1

    def pop(self):
        if self.empty():
            return 'Fila vazia'
        elem = self.first.data
        self.first = self.first.next # se o primeiro saiu aponta para o proximo

        if self.first is None: # se o ultimo elemento for None, tem que corrigir o next tbem
            self.last = None # zera o next

        self._size -= 1 # diminui o tamanho do size
        return elem

    def peek(self):
        if self.empty():
            return 'Fila vazia'
        return self.first.data # primeiro que entra, primeiro que sai

    def __len__(self):
        return self._size

    def empty(self):
        return len(self) == 0

    def __repr__(self):
        if self.empty():
            return 'Fila vazia'

        string = ''
        ponteiro = self.first
        while(ponteiro):
            string += str(ponteiro.data) + '\n' 
            ponteiro = ponteiro.next
          
        if(ponteiro): 
            string += ' -> '
        return string

fila = Queue()



fila.push ('José')
fila.push ('Maria')
fila.push ('Josicreide')
fila.push ('Emengarda')

print (fila)

fila.pop()
print (fila)

