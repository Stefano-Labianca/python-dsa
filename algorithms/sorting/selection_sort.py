def selection_sort(nums: list[int]):
    for i in range(len(nums)):
        smallest_idx = i

        for j in range(smallest_idx + 1, len(nums)):
            if nums[j] < nums[smallest_idx]:
                smallest_idx = j

        nums[i], nums[smallest_idx] = nums[smallest_idx], nums[i]
