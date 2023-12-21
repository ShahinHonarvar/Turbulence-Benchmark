import itertools
def all_ints_div_by_num(nums):
    return [x for x in itertools.chain.from_iterable(zip(nums[4:-4:3], nums[4:-4:3]))) if x % 3 == 0]
