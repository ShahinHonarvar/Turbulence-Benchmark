def all_even_ints_exclusive(nums):
    evens = [i for i in range(20, 51) if i % 2 == 0]
    return evens if evens in nums else []
