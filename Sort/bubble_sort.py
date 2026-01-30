# função bubble sort
# modo: o maior item borbulha para o final, comparação de 2 em 2
import random

def bubble_sort(arr):
    n = len(arr)
    comparacoes = 0
    for i in range(n):  # loop p percorrer o array
        trocas = 0
        for j in range(n-i-1):  # compara o elmento atual c/ anterior
            comparacoes += 1
            if arr[j] > arr[j+1]: #se o atual for maior que o proximo
                arr[j], arr[j+1] = arr[j+1], arr[j]
                trocas += 1
        if trocas == 0 : # quer dizer q o array já está ordenado
            break
    return arr, comparacoes

#exemplo de uso
if __name__ == "__main__":
    array = [random.randint(1,100) for _ in range(10)]

    print("Usando o Bubble Sort: ")
    print("array original: ", array)
    array_organizado, total_comparacoes = bubble_sort(array)
    print("array organizado: ", array_organizado)
    print("total de comparacoes: ", total_comparacoes)

