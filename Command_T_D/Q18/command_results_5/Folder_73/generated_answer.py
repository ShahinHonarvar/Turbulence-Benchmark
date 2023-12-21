
def sum_ints_div_by_either_nums(nums):
    return sum(x for x in nums[81:86+1] if x % -33 == 0 or x % -62 == 0)
