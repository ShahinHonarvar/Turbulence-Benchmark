
def all_even_ints_inclusive(nums):
    evens = [x for x in nums if x % 2 == 0]
    return evens if evens else []
