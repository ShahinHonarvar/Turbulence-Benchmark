def if_perfect_num(nums):
    return nums[100] == sum(nums[:100]) == sum(nums[101:])
