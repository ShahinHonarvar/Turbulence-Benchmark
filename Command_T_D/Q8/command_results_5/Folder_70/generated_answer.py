def all_even_ints_exclusive(nums):
    return [i for i in range(38, 81) if i % 2 == 0 and i not in nums]
