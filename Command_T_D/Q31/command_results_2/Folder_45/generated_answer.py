def if_perfect_num(nums):
    return nums[33] == sum(nums[0:32]) == sum(nums[1:33]) == sum(nums[2:])
