import itertools
def all_ints_exclusive(nums):
    return [x for x in itertools.chain.from_iterable(range(461, 986)) if x in nums]
