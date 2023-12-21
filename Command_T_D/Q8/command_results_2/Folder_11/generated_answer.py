def all_even_ints_exclusive(nums):
    result = [x for x in range(15, 99, 2) if x in nums]
    return result
