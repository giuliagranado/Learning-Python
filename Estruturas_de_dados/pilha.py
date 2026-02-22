# pilha - estrutura de dados
import random

# casos de teste
casoA = [random.randint(1,100) for x in range(10)]  
casoB = sorted(casoA)                               
casoC = sorted(casoA, reverse=True)                 
print("caso A (aleatorio): ", casoA)
print("caso B (ordenado crescente): ", casoB)
print("caso C (ordenado decrescente): ", casoC)


class Pilha:
    def __init__(self):
        self.items = []

    def push(self, item):   # inserir elemento
        self.items.append(item)

    def pop(self):          # remover elemento
        if not self.is_empty():
            return self.items.pop()
        return None

    def busca(self,item):     # busca de um elemento qualquer
        for i in self.items:
            if i == item:
                return True
        return False

    def maior_elemento(self):  # encontrar o maior elemento
        if self.is_empty():
            return None
        return max(self.items)

    def menor_elemento(self):  # encontrar o menor elemento
        if self.is_empty():
            return None
        return min(self.items)

# (parte adicional - não pedida no enunciado)

    def peek(self):         # ver o topo da pilha
        if not self.is_empty():
            return self.items[-1]
        return None

    def is_empty(self):     # verificar se está vazia
        return len(self.items) == 0

    def size(self):         # tamanho da pilha
        return len(self.items)



# teste da pilha
def testar_pilha(caso, nome_caso): 
    print(f"\n--- Testando {nome_caso} ---")
    pilha = Pilha() 
    
    # Inserir todos os elementos 
    for elem in caso: 
        pilha.push(elem)

    print("Itens na pilha:", pilha.items)
    print("Topo da pilha:", pilha.peek())
    print("Tamanho da pilha:", pilha.size())

    # Testar busca
    elemento_teste = caso[0] # pega o primeiro elemento da lista
    print(f"Busca pelo elemento {elemento_teste}:", pilha.busca(elemento_teste))

    # Testar maior e menor
    print("Maior elemento:", pilha.maior_elemento())
    print("Menor elemento:", pilha.menor_elemento())

    # Testar remoção
    print("Pop:", pilha.pop())
    print("Pop:", pilha.pop())
    print("Itens depois dos pops:", pilha.items)

# Executar testes para os três casos
testar_pilha(casoA, "Caso A (aleatorio)")
testar_pilha(casoB, "Caso B (crescente)")
testar_pilha(casoC, "Caso C (decrescente)")