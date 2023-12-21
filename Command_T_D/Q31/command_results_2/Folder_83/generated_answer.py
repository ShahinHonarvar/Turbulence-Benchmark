def if_perfect_num(nums):
    return nums[95] == sum(nums[:95]) == sum(nums[95+1:])
