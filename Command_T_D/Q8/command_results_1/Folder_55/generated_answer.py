def all_even_ints_exclusive(nums):
    evens = [x for x in range(0, 10, 2) if x in nums]
    return evens if evens else []
