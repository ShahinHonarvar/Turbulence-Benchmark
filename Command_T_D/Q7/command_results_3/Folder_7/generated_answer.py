
def all_even_ints_inclusive(nums):
    return [i for i in range(661, 924 + 1) if i % 2 == 0 and i in nums]
