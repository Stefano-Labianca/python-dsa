def bubble_sort(arr: list) -> list:
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