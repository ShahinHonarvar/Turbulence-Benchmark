def if_perfect_num(nums):
    return nums[48] == sum(nums[:48]) == sum(nums[48+1:])
