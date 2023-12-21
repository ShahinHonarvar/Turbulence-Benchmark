
def all_even_ints_inclusive(nums):
    return [x for x in range(639, 975 + 1) if x % 2 == 0 and x in nums]
