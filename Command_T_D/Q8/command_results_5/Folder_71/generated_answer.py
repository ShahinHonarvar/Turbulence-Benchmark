def all_even_ints_exclusive(nums):
    result = []
    for index in range(36, 54):
        if index % 2 == 0:
            result.append(nums[index])
    return result
