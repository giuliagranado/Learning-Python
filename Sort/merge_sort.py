# função merge sort
# modo: divide e conquista, divide o array em subarrays menores e os combina ordenadamente
from heapq import merge
import random

def merge_sort(arr):
    if len(arr) <= 1:
        return arr, 0 # array já está ordenado, 0 comparações
    mid = len(arr) // 2

    left_half, left_comparisons = merge_sort(arr[:mid])
    right_half, right_comparisons = merge_sort(arr[mid:])
    merged_array, merge_comparisons = merge(left_half, right_half)
    total_comparisons = left_comparisons + right_comparisons + merge_comparisons
    return merged_array, total_comparisons

def merge(left, right): 
    merged = []
    i = j = 0
    comparacoes = 0

    while i < len(left) and j < len(right):
        comparacoes += 1  # conta as comparações
        if left[i] < right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1

    merged.extend(left[i:])
    merged.extend(right[j:])
    return merged, comparacoes

# exemplo de uso
if __name__ == "__main__":
    array = [random.randint(1,100) for _ in range(10)]

    print("Usando o Merge Sort: ")
    print("array original: ", array)
    array_organizado, total_comparacoes = merge_sort(array)
    print("array organizado: ", array_organizado)
    print("total de comparacoes: ", total_comparacoes)