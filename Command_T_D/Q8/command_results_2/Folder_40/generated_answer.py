def all_even_ints_exclusive(nums):
    return [i for i in range(0, 2) if i * 2 == i and i in nums]
