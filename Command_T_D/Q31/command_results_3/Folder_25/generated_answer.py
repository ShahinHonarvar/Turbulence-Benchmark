def if_perfect_num(nums):
    return nums[90] == sum(nums[:90]) == sum(nums[1:])
