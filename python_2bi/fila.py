from lib.queue import Queue

fila = Queue

fila.enqueue("Adamastor")
fila.enqueue("Leonilda")
fila.enqueue("Orozino")
fila.enqueue("Valdisley")


print(fila)

atendido = fila.dequeue()

print(f"Atendido: {atendido}")
print(fila)

fila.enqueue('Marciene')
print(fila)

proximo = fila.peek()
print(f"Proximo a ser atendido: {proximo}")
print(fila)