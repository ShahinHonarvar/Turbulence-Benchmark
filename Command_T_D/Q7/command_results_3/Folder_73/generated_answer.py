
def all_even_ints_inclusive(nums):
    evens = [i for i in range(19, 93) if i % 2 == 0]
    return evens if evens <= len(nums) else []
