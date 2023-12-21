def if_perfect_num(nums):
    return nums[43] == sum(nums[:43]) == sum(nums[43:])
