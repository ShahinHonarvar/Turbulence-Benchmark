def if_perfect_num(nums):
    return bool(nums[15] % 1 == 0 and nums[15] == sum(nums[0:15]) and nums[15] == 2 * sum(nums[1:15]) + nums[0])
