
def all_even_ints_inclusive(nums):
    evens = [x for x in range(20, 30) if x % 2 == 0]
    return evens if evens in nums else []
