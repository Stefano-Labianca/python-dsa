# from algorithms.sorting.insertion_sort import insertion_sort
# from algorithms.sorting.merge_sort import merge_sort
# from algorithms.sorting.bubble_sort import bubble_sort

from algorithms.sorting.quick_sort import quick_sort

arr = [9, 6, 2, 1, 8, 7]

# print(
#     f"Bubble Sort: {bubble_sort(arr)}", f"Merge Sort: {merge_sort(arr)}",
#     f"Insertion Sort: {insertion_sort(arr)}" ,
#     sep="\n"
# )


quick_sort(arr, 0, len(arr) - 1)
print(arr)