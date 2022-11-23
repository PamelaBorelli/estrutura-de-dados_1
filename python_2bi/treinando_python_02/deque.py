# fusão de pilha e fila, os elementos podem ser retirados tanto no inicio quanto no fim. 

# deck = size, left, right
# node = são cada elementos (data, previous, next)

# push = inclui
# pop = elimina
# top ou peek = mostra quem aparece no extremo
# no caso precisa da orientação left ou right

class Node:
    def __init__(self, data):
        self.data = data
        self.previous = None
        self.next = None

class Deck:
    def __init__(self):
        self.left = None
        self.right = None
        self._size = 0

    def push_left(self, elem):

        node = Node(elem)

        if self.left is None:
            self.left = node
            self.right = node
        else: 
            self.left.previous = node
            node.next = self.left 
            self.left = node
        self._size +=1


    def push_right(self, elem):

        node = Node(elem)

        if self.right is None:
            self.right = node
            self.left = node
        else: 
            node.previous = self.right 
            self.right.next = node
            self.right = node
        self._size +=1

    def pop_left(self):
        if self.empty():
            return 'Deque vazio'
        elem = self.left.data   #armazena o atual left
        self.left = self.left.next #nodifica o atual left para o next
        self.left.previous = None # pegamos o previous e colocamos None
        self._size -=1
        return elem

    def pop_right(self):
        if self.empty():
            return len(self) == 0
        elem = self.right.data   #armazena o atual left
        self.right = self.right.previous #nodifica o atual left para o next
        self.right.next = None # pegamos o previos e colocamos None
        self._size -=1
        return elem

    def peek_left(self):
        if self.empty():
            return 'Deque vazio'
        return self.left.data   #armazena o atual left
        

    def peek_right(self):
        if self.empty():
            return len(self) == 0
        return self.right.data   #armazena o atual left
        
  
    def __len__(self): # sobrecarga de operador (serve para usa um operador de um objeto do prograna )
        return self._size

    def empty(self):
        return len(self) == 0

    def __repr__ (self):
        if self.empty():
            return 'Deque Vazio'

        
        ponteiro = self.left
        string = 'left <<'
        while(ponteiro):
            string += str(ponteiro.data)
            ponteiro = ponteiro.next
          
            if(ponteiro): 
                string += ' | '
        string += ' >> right'
        return string


deque = Deck()
# print (deque)

# print (deque.empty)
# print (deque.push_left)

deque.push_left(5)

# print (deque)

deque.push_left(4)
print (deque)

deque.push_right(6)
print (deque)

# deque.pop_left()
# print (deque)

# deque.pop_right()
# print (deque)

deque.peek_right()
print(deque)

  