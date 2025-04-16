def quick_sort(nums: list[int], low: int, high: int):
    if low < high:
        middle = __partition(nums, low, high)

        quick_sort(nums, low, middle - 1)
        quick_sort(nums, middle + 1, high)


def __partition(nums: list[int], low: int, high: int) -> int:
    pivot = nums[high]
    i = low - 1
    
    for j in range(low, high):
        if nums[j] < pivot:
            i += 1
            nums[i], nums[j] = nums[j], nums[i]

    new_pivot_idx = i + 1
    nums[new_pivot_idx], nums[high] = nums[high], nums[new_pivot_idx]

    return new_pivot_idx