# função insertion sort
# modo: constrói o array ordenado um elemento por vez
import random

def insertion_sort(array):
    n = len(array)
    comparacoes = 0
    for i in range(n):
        key = array[i]
        j = i -1 

        while j >= 0:    #compara e desloca enquanto necessario
            comparacoes += 1 # conta as comparações
            if array[j] > key:
                array[j + 1] = array[j]
                j -= 1
            else:    # saí do laço se ñ precisa trocar
                break 
    return array, comparacoes

# exemplo de uso
if __name__ == "__main__":
    array = [random.randint(1,100) for _ in range(10)]

    print("Usando o Insertion Sort: ")
    print("array original: ", array)
    array_organizado, total_comparacoes = insertion_sort(array)
    print("array organizado: ", array_organizado)
    print("total de comparacoes: ", total_comparacoes)
