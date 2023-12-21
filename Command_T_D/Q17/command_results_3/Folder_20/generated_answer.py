
def all_ints_div_by_both_two_nums(nums):
    return [i for i in range(48, 76) if (i % -46 == 0 and i % -82 == 0) and i in nums]
