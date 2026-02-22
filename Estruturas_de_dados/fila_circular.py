# fila circular - estrtura de dados
import random

# casos de teste
casoA = [random.randint(1,100) for x in range(10)]  
casoB = sorted(casoA)                               
casoC = sorted(casoA, reverse=True)                 
print("caso A (aleatorio): ", casoA)
print("caso B (ordenado crescente): ", casoB)
print("caso C (ordenado decrescente): ", casoC)


class FilaCircular:
    def __init__(self, capacidade):
        self.capacidade = capacidade
        self.fila = [None] * capacidade
        self.inicio = 0
        self.fim = -1
        self.tamanho = 0

    def is_empty(self):
        return self.tamanho == 0

    def is_full(self):
        return self.tamanho == self.capacidade

    def enqueue(self, item):  # inserir elemento
        if self.is_full():
            print("Fila cheia! Não é possível inserir.")
            return
        self.fim = (self.fim + 1) % self.capacidade
        self.fila[self.fim] = item
        self.tamanho += 1

    def dequeue(self):        # remover elemento
        if self.is_empty():
            print("Fila vazia! Não é possível remover.")
            return None
        item = self.fila[self.inicio]
        self.fila[self.inicio] = None
        self.inicio = (self.inicio + 1) % self.capacidade
        self.tamanho -= 1
        return item

    def peek(self):           # ver o primeiro elemento
        if self.is_empty():
            return None
        return self.fila[self.inicio]

    def maior_elemento(self):
        if self.is_empty():
            return None
        return max([x for x in self.fila if x is not None])

    def menor_elemento(self):
        if self.is_empty():
            return None
        return min([x for x in self.fila if x is not None])

    def busca(self, item):
        return item in [x for x in self.fila if x is not None]

    def __str__(self):
        return str([x for x in self.fila if x is not None])

# função de teste genérica
def testar_fila(caso, nome_caso):
    print(f"\n--- Testando {nome_caso} ---")
    fila = FilaCircular(len(caso))

    # inserir todos os elementos
    for elem in caso:
        fila.enqueue(elem)

    print("Itens na fila:", fila)
    print("Primeiro da fila:", fila.peek())
    print("Tamanho da fila:", fila.tamanho)

    # testar busca
    elemento_teste = caso[0]
    print(f"Busca pelo elemento {elemento_teste}:", fila.busca(elemento_teste))

    # testar maior e menor
    print("Maior elemento:", fila.maior_elemento())
    print("Menor elemento:", fila.menor_elemento())

    # testar remoção
    print("Dequeue:", fila.dequeue())
    print("Dequeue:", fila.dequeue())
    print("Itens depois dos dequeues:", fila)

# executar testes para os três casos
testar_fila(casoA, "Caso A (aleatório)")
testar_fila(casoB, "Caso B (crescente)")
testar_fila(casoC, "Caso C (decrescente)")

