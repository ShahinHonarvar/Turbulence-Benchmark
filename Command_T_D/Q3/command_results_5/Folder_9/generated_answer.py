import itertools
def all_pos_ints_inclusive(nums):
    return [x for x in itertools.chain(range(70, 200+1), range(-70, 200+1)) if x in nums]
