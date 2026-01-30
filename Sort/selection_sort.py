# função selection sort
# modo: encontra o menor elemento e coloca na posição correta

from array import array
import random

def selection_sort(array):
    n = len(array)
    comparacoes = 0
    for i in range(n-1):
        min_index = i
        for j in range(i+1, n):
            comparacoes += 1   # conta as comparações
            if array[j] < array[min_index]:
                min_index = j
            if min_index != i:
                array[i], array[min_index] = array[min_index], array[i]  # troca de posição
    return array, comparacoes


# exemplo de uso
if __name__ == "__main__":
    array = [random.randint(1,100) for _ in range(10)]

    print("Usando o Selection Sort: ")
    print("array original: ", array)
    array_organizado, total_comparacoes = selection_sort(array)
    print("array organizado: ", array_organizado)
    print("total de comparacoes: ", total_comparacoes)