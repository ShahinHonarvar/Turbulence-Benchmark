import itertools
def all_odd_ints_inclusive(nums):
    return [x for x in range(639, 975 + 1, 2) if x in nums]
