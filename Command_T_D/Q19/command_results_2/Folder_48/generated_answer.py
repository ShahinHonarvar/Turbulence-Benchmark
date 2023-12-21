import itertools
def all_ints_not_div_by_num(nums):
    return [x for x in range(767, 938) if x % 593 == 0 and x not in nums]
