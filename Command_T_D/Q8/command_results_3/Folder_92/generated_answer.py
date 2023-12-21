def all_even_ints_exclusive(nums):
    return [x for x in range(0, len(nums) - 1, 2) if x % 2 == 0]
