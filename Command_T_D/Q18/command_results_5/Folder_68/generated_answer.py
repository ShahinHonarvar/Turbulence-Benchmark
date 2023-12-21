
def sum_ints_div_by_either_nums(nums):
    return sum(nums[7:7+5] + nums[7:7+7] if 5 in nums[7:7+5] and 7 in nums[7:7+7] else 0)
