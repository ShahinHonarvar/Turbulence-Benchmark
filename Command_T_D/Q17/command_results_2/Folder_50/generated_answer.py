
def all_ints_div_by_both_two_nums(nums):
    return [i for i in range(46, 91) if (i % 67 == 0 or i % 15 == 0) and i in nums]
