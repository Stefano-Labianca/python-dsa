from typing import TypeVar

T = TypeVar('T', int, str, float)

def bubble_sort(arr: list[T]) -> list[T]:
    swapping = True
    end = len(arr)

    while swapping:
        swapping = False

        for i in range(1, end):
            if arr[i - 1] > arr[i]:
                arr[i - 1], arr[i] = arr[i], arr[i - 1]
                swapping = True

        end -= 1
        
    return arr