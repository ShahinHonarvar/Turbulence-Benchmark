def all_even_ints_exclusive(nums):
    result = []
    for i in range(598, 767):
        if nums[i] % 2 == 0:
            result.append(nums[i])
    return result
