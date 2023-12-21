import itertools
def all_pos_ints_inclusive(nums):
    return [x for x in itertools.chain(nums[82:], nums[83:], nums[84:], nums[85:], nums[86:]) if x > 0]
