def all_even_ints_exclusive(nums):
    evens = [e for e in range(20, 43) if e % 2 == 0]
    return evens if evens in nums else []
