from algorithms.sorting.merge_sort import merge_sort
from algorithms.sorting.bubble_sort import bubble_sort

arr = [9, 8, 7, 6, 5, 4, 3, 2, 1]

print(
    f"Bubble Sort: {bubble_sort(arr)}", f"Merge Sort: {merge_sort(arr)}", 
    sep="\n"
)


