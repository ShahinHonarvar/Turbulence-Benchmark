def if_perfect_num(nums):
    return nums[88] == sum(nums[0:88]) == sum(nums[88+1:])
