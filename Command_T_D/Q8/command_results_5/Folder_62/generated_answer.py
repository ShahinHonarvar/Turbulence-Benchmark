def all_even_ints_exclusive(nums):
    even_ints = [i for i in range(55, 85) if i % 2 == 0]
    return [e for e in even_ints if e in nums]
