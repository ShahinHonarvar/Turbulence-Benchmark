import itertools
def all_odd_ints_exclusive(nums):
    return [x for x in range(361, 643, 2) if x in nums]
