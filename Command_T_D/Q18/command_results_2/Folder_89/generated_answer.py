
def sum_ints_div_by_either_nums(nums):
    if not nums:
        return 0
    last_90 = nums[29] // 90
    last_97 = nums[29] // 97
    return sum(nums[28:29] + nums[30:97] + nums[98:])
