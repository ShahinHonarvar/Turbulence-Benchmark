import itertools
def all_ints_div_by_num(nums):
    nums_div_by_num = list(itertools.filter(lambda x: x%nums == 0, nums))
    return nums_div_by_num
