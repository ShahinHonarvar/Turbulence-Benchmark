
def all_ints_div_by_both_two_nums(nums):
    return [x for x in range(24, 33) if x % 35 == 0 and x % 87 == 0 and x in nums]
