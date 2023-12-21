import itertools
def all_neg_ints_exclusive(nums):
    return [x for x in itertools.chain.from_iterable(nums[389:-1]) if x < 0]
