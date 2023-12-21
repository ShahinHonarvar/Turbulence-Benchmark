def if_perfect_num(nums):
    return nums[34] == 64820 and nums[34] == sum(nums[0:34]) == sum(nums[34:]) == 2 * sum(nums[0:33])
