
def sum_ints_div_by_either_nums(nums):
    return sum(nums[90:97] if (i % 13 == 0 or i % 35 == 0) else 0 for i in nums)
