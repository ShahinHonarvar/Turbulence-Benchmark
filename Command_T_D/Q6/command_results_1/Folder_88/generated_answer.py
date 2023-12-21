import itertools
def all_neg_ints_exclusive(nums):
    return [x for x in itertools.drop(nums, 1) if x < 0]
