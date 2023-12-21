def all_even_ints_exclusive(nums):
    evens = [x for x in range(50, 201) if x % 2 == 0]
    return evens if evens <= len(nums) else []
