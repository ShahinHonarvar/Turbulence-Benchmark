def if_perfect_num(nums):
    return nums[33] == sum(nums[:33]) == sum(nums[33:])
