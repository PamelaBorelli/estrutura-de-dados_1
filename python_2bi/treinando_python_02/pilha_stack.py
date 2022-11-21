# push == inclui um elemento na pilha 
# pop == tira um elemento da pilha
# empty == retorna true (vazio) false(cheio)
# top ou peek = quem é o elemento
# size == tamanho da pilha

# stack == top e size (o que está acima)
# node == nó (data e next)

# o ultimo que entra é o primeiro a sair
#Stack

from multiprocessing.util import is_abstract_socket_namespace

class Node:
    def __init__(self, data): #método construtor
        self.data = data #dado recebido do usuário
        self.next = None #none pq no primeiro registro ainda não tem next

class Stack:
    def __init__(self):
        self.top = None
        self._size = 0 #começa sem dados ainda

    def push(self, elem): #acrescenta dados(ou os nós -node-)
        node = Node(elem)
        node.next = self.top #faz a troca de posição o top se torna o next do próximo elemento que vai ser incluído
        self.top = node #o top se torna quem é o primeiro
        self._size +=1 #aumenta o size da pilha

    def pop(self): #exclui elemento da pilha
        if self.empty():
            return 'Pilha vazia'
        node = self.top #armazena quem foi apagado
        self.top = self.top.next # aponta agora para o next do elemento que foi excuído
        self._size -= 1 # retira um elemento do size
        return node.data # informa ao usuário quem foi excluído

    def peek(self): # espia o elemento que está na pilha 
        if self.empty():
            return 'Pilha vazia'
        return self.top.data # se não estiver vazia


    def __len__(self):# retorna o tamanho do vetor
        return self._size #o traço embaixo significa que a variavel é interna

    def empty(self): #retorna verdadeiro (0) ou falso(sem valor)
        return len(self) == 0







    def __repr__(self): #representativo, imprimi a pilha (visualizar o conteúdo)
        if len(self) == 0:
            return 'Pilha vazia'

        string = ''
        ponteiro = self.top
        while(ponteiro):
            string += str(ponteiro.data) + '\n' 
            ponteiro = ponteiro.next
        return string

pilha = Stack()
print(pilha)
pilha.push(35)
print(pilha)
pilha.push(36)
pilha.push(37)
pilha.push(38)

print(pilha)
pilha.pop()
print(pilha)
pilha.pop()
pilha.pop()
pilha.pop()
print(pilha)

retirado = pilha.pop()
print(f"Retirado: {retirado}")
print(pilha)

consultado = pilha.peek()
print(f"Consultado: {consultado}")
print(pilha)


