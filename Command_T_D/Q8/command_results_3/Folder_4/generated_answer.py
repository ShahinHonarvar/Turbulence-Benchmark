def all_even_ints_exclusive(nums):
    evens = [x for x in range(10, 76) if x % 2 == 0]
    return evens if evens in nums else []
