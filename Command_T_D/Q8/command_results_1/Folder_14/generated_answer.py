def all_even_ints_exclusive(nums):
    evens = [x for x in range(2, 8) if x % 2 == 0]
    return [x for x in evens if x in nums]
