import itertools
def all_ints_div_by_num(nums):
    return [x for x in itertools.takewhile(lambda x: x % 77 == 0, nums[66:81]) if x]
