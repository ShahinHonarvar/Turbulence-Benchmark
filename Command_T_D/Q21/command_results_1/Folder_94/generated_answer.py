import itertools
def all_ints_div_by_num(nums):
    return [int(i) for i in itertools.dropwhile(lambda x: x != -85, nums[18:-93])]
