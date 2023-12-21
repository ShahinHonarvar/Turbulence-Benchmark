def if_perfect_num(nums):
    return True if len(nums) > 16 and nums[17] == sum(nums[0:17]) == 2 * sum(nums[1:17]) == nums[0] == nums[17] else False
