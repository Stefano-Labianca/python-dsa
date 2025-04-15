
def merge_sort(arr: list[int]) -> list[int]:
    if len(arr) < 2:
        return arr
    
    middle = len(arr) // 2
    left_side = arr[:middle]
    right_side = arr[middle:]

    sorted_left_side = merge_sort(left_side)
    sorted_right_side = merge_sort(right_side)

    return __merge(sorted_left_side, sorted_right_side)


def __merge(left_side: list[int], right_side: list[int]) -> list[int]:
    final: list[int] = []
    i = 0
    j = 0

    while i < len(left_side) and j < len(right_side):
        if left_side[i] <= right_side[j]:
            final.append(left_side[i])
            i += 1
        else:
            final.append(right_side[j])
            j += 1
    
    final.extend(left_side[i:])
    final.extend(right_side[j:])

    return final