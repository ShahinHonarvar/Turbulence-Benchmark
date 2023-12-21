def all_even_ints_exclusive(nums):
    result = []
    for i in range(10, 80, 2):
        if i in nums:
            result.append(i)
    return result
