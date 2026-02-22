# arvore binaria - estrutura de dados
'''A árvore binária organiza os elementos de forma hierárquica: cada nó tem até dois filhos, e na versão de busca, os valores menores ficam à esquerda e os maiores à direita. Isso facilita operações como busca, inserção e remoção.'''

import random

# casos de teste
casoA = [random.randint(1,100) for x in range(10)]  
casoB = sorted(casoA)                               
casoC = sorted(casoA, reverse=True)                 
print("caso A (aleatório): ", casoA)
print("caso B (ordenado crescente): ", casoB)
print("caso C (ordenado decrescente): ", casoC)

# nó da árvore binária
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class ArvoreBinaria:
    def __init__(self):
        self.root = None

    def inserir(self, data):
        if self.root is None:
            self.root = Node(data)
        else:
            self._inserir(self.root, data)

    def _inserir(self, atual, data):
        if data < atual.data:
            if atual.left is None:
                atual.left = Node(data)
            else:
                self._inserir(atual.left, data)
        else:
            if atual.right is None:
                atual.right = Node(data)
            else:
                self._inserir(atual.right, data)

    def busca(self, data):
        return self._busca(self.root, data)

    def _busca(self, atual, data):
        if atual is None:
            return False
        if atual.data == data:
            return True
        elif data < atual.data:
            return self._busca(atual.left, data)
        else:
            return self._busca(atual.right, data)

    def maior_elemento(self):
        atual = self.root
        if atual is None:
            return None
        while atual.right:
            atual = atual.right
        return atual.data

    def menor_elemento(self):
        atual = self.root
        if atual is None:
            return None
        while atual.left:
            atual = atual.left
        return atual.data

    def inorder(self):  # percurso em ordem crescente
        elementos = []
        self._inorder(self.root, elementos)
        return elementos

    def _inorder(self, atual, elementos):
        if atual:
            self._inorder(atual.left, elementos)
            elementos.append(atual.data)
            self._inorder(atual.right, elementos)


# função de teste genérica
def testar_arvore(caso, nome_caso):
    print(f"\n--- Testando {nome_caso} ---")
    arvore = ArvoreBinaria()

    # inserir todos os elementos
    for elem in caso:
        arvore.inserir(elem)

    print("Elementos em ordem (inorder):", arvore.inorder())
    print("Busca pelo primeiro elemento:", arvore.busca(caso[0]))
    print("Maior elemento:", arvore.maior_elemento())
    print("Menor elemento:", arvore.menor_elemento())


# executar testes para os três casos
testar_arvore(casoA, "Caso A (aleatório)")
testar_arvore(casoB, "Caso B (crescente)")
testar_arvore(casoC, "Caso C (decrescente)")
