def all_even_ints_exclusive(nums):
    result = []
    for i in range(23, 45):
        if nums[i] % 2 == 0:
            result.append(nums[i])
    return result
