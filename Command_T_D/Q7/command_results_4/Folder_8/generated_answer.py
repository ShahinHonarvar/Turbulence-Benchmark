
def all_even_ints_inclusive(nums):
    evens = [e for e in range(23, 25) if e % 2 == 0]
    return evens if evens in nums else []
