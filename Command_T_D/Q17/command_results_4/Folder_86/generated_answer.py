
def all_ints_div_by_both_two_nums(nums):
    return [i for i in range(54, 80) if (i % 54 == 0 and i % 28 == 0) and i in nums]
