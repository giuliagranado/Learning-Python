# lista duplamente ligadaCircular (sem sentinela) - estrutura de dados
import random

# casos de teste
casoA = [random.randint(1,100) for x in range(10)]  
casoB = sorted(casoA)                               
casoC = sorted(casoA, reverse=True)                 
print("caso A (aleatório): ", casoA)
print("caso B (ordenado crescente): ", casoB)
print("caso C (ordenado decrescente): ", casoC)


# Nó da lista duplamente ligada
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


# Lista duplamente ligada circular
class ListaDuplamenteLigadaCircular:
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head is None

    def inserir(self, data):  # insere no final
        novo = Node(data)
        if self.is_empty():
            self.head = novo
            novo.next = novo
            novo.prev = novo
        else:
            tail = self.head.prev
            tail.next = novo
            novo.prev = tail
            novo.next = self.head
            self.head.prev = novo

    def remover(self, data):  # remove o primeiro nó com valor igual
        if self.is_empty():
            return False
        atual = self.head
        while True:
            if atual.data == data:
                if atual.next == atual:  # só um nó
                    self.head = None
                else:
                    atual.prev.next = atual.next
                    atual.next.prev = atual.prev
                    if atual == self.head:
                        self.head = atual.next
                return True
            atual = atual.next
            if atual == self.head:
                break
        return False

    def busca(self, data):
        if self.is_empty():
            return False
        atual = self.head
        while True:
            if atual.data == data:
                return True
            atual = atual.next
            if atual == self.head:
                break
        return False

    def maior_elemento(self):
        if self.is_empty():
            return None
        atual = self.head
        maior = atual.data
        while True:
            if atual.data > maior:
                maior = atual.data
            atual = atual.next
            if atual == self.head:
                break
        return maior

    def menor_elemento(self):
        if self.is_empty():
            return None
        atual = self.head
        menor = atual.data
        while True:
            if atual.data < menor:
                menor = atual.data
            atual = atual.next
            if atual == self.head:
                break
        return menor

    def __str__(self):
        if self.is_empty():
            return "[]"
        elementos = []
        atual = self.head
        while True:
            elementos.append(atual.data)
            atual = atual.next
            if atual == self.head:
                break
        return str(elementos)


# Função de teste genérica
def testar_lista(caso, nome_caso):
    print(f"\n--- Testando {nome_caso} ---")
    lista = ListaDuplamenteLigadaCircular()

    # Inserir todos os elementos
    for elem in caso:
        lista.inserir(elem)

    print("Itens na lista:", lista)
    print("Busca pelo primeiro elemento:", lista.busca(caso[0]))
    print("Maior elemento:", lista.maior_elemento())
    print("Menor elemento:", lista.menor_elemento())

    # Remover dois elementos
    print("Removendo:", caso[0], "->", lista.remover(caso[0]))
    print("Removendo:", caso[-1], "->", lista.remover(caso[-1]))
    print("Itens após remoções:", lista)


# Executar testes para os três casos
testar_lista(casoA, "Caso A (aleatório)")
testar_lista(casoB, "Caso B (crescente)")
testar_lista(casoC, "Caso C (decrescente)")
