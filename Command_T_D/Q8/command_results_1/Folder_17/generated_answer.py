def all_even_ints_exclusive(nums):
    even_ints = [x for x in range(62, 96) if x % 2 == 0]
    return [x for x in even_ints if x in nums]
