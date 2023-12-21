def all_even_ints_exclusive(nums):
    result = []
    for i in range(20, 36):
        if i % 2 == 0:
            result.append(nums[i])
    return result
