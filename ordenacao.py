# exercicios dia 06.03.26
import randon

# 1
listaA = []

def insertion_sort(listaA):
    for i in range(1, len(listaA)):
        chave = listaA[i]
        j = i - 1
        # Move os elementos maiores que a chave uma posição à frente
        while j >= 0 and listaA[j] > chave:
            listaA[j + 1] = listaA[j]
            j -= 1
        listaA[j + 1] = chave
    return listaA

# Exemplo de uso
numeros = [5, 2, 9, 1, 5, 6]
ordenados = insertion_sort(numeros)
print(ordenados)  # Saída: [1, 2, 5, 5, 6, 9]


for i in range(50): 
    numero = random.randint(1, 100)
    listaA.append(numero)
