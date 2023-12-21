def all_even_ints_exclusive(nums):
    return [i for i in range(100, 101) if i % 2 == 0 and i in nums]
