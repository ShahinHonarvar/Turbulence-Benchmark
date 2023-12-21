
def sum_ints_div_by_either_nums(nums):
    return sum(x for x in nums if x % -5 == 0 or x % -6 == 0)
