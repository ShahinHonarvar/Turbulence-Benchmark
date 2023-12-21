def if_perfect_num(nums):
    return nums[24] == sum(nums[:24]) == sum(nums[24:])
