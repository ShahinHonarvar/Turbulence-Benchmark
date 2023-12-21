def if_perfect_num(nums):
    return bool(nums[1] == sum(nums[2:]) and nums[1] == nums[0] + nums[1] and nums[0] == 1)
