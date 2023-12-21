
def all_even_ints_inclusive(nums):
    evens = [e for e in range(6, len(nums) + 1, 2) if e in nums]
    return evens if evens else []
