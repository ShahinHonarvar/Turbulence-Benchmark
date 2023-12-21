def composite_nums_between_indices(nums):
    result = set()
    for i in range(2, 5):
        for j in range(2, int(nums[i] ** .5) + 1):
            if nums[i] % j == 0:
                result.add(nums[i] * j)
    return result
