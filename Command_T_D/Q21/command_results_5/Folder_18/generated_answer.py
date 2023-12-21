import itertools
def all_ints_div_by_num(nums):
    return [x for x in range(26, 75) if x % 80 in nums]
