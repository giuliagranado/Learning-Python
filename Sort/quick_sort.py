# função quick sort
# modo: divide e conquista, escolhe um pivô e particiona o array em elementos menores e maiores que o pivô
import random

def quick_sort(arr):
    if len(arr) <= 1:
        return arr, 0   # array já está ordenado e 0 comparações
    pivot = arr[len(arr)//2]
    left = []
    middle = []
    right = []
    comparacoes = 0

    for x in arr:
        comparacoes += 1  # conta as comparações
        if x < pivot:
            left.append(x)
        elif x == pivot:
            middle.append(x)
        else:
            right.append(x)

    left_sorted, left_comparisons = quick_sort(left)
    right_sorted, right_comparisons = quick_sort(right)
    total_comparisons = comparacoes + left_comparisons + right_comparisons
    return left_sorted + middle + right_sorted, total_comparisons

# exemplo de uso
if __name__ == "__main__":
    array = [random.randint(1,100) for _ in range(10)]

    print("Usando o Quick Sort: ")
    print("array original: ", array)
    array_organizado, total_comparacoes = quick_sort(array)
    print("array organizado: ", array_organizado)
    print("total de comparacoes: ", total_comparacoes)