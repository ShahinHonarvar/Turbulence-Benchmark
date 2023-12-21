
def sum_ints_div_by_either_nums(nums):
    return sum(x for x in nums[20:93] if x % -92 == 0 or x % -50 == 0)
