# lista duplamente ligadaCircular (com sentinela) - estrutura de dados
# sentinela = nó especial sem dados válidos, facilita as operações, servindo de ref fixa

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
    def __init__(self, data=None):
        self.data = data
        self.next = None
        self.prev = None


# Lista duplamente ligada circular com sentinela
class ListaDuplamenteLigadaCircularSentinela:
    def __init__(self):
        self.sentinela = Node()  # nó especial
        self.sentinela.next = self.sentinela
        self.sentinela.prev = self.sentinela

    def is_empty(self):
        return self.sentinela.next == self.sentinela

    def inserir(self, data):  # insere no final
        novo = Node(data)
        ultimo = self.sentinela.prev
        ultimo.next = novo
        novo.prev = ultimo
        novo.next = self.sentinela
        self.sentinela.prev = novo

    def remover(self, data):  # remove o primeiro nó com valor igual
        atual = self.sentinela.next
        while atual != self.sentinela:
            if atual.data == data:
                atual.prev.next = atual.next
                atual.next.prev = atual.prev
                return True
            atual = atual.next
        return False

    def busca(self, data):
        atual = self.sentinela.next
        while atual != self.sentinela:
            if atual.data == data:
                return True
            atual = atual.next
        return False

    def maior_elemento(self):
        if self.is_empty():
            return None
        atual = self.sentinela.next
        maior = atual.data
        while atual != self.sentinela:
            if atual.data > maior:
                maior = atual.data
            atual = atual.next
        return maior

    def menor_elemento(self):
        if self.is_empty():
            return None
        atual = self.sentinela.next
        menor = atual.data
        while atual != self.sentinela:
            if atual.data < menor:
                menor = atual.data
            atual = atual.next
        return menor

    def __str__(self):
        elementos = []
        atual = self.sentinela.next
        while atual != self.sentinela:
            elementos.append(atual.data)
            atual = atual.next
        return str(elementos)


# Função de teste genérica
def testar_lista(caso, nome_caso):
    print(f"\n--- Testando {nome_caso} ---")
    lista = ListaDuplamenteLigadaCircularSentinela()

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
