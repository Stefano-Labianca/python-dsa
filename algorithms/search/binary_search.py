def binary_search(arr: list[int], target: int) -> int:
    low = 0
    high = len(arr) - 1

    while low <= high:
        middle = (low + high) // 2

        if arr[middle] == target:
            return middle
        
        if arr[middle] < target:
            low = middle + 1
        else:
            high = middle - 1

    return -1