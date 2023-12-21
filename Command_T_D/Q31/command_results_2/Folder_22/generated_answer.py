def if_perfect_num(nums):
    return nums[72] == sum(nums[i: i + i]) == sum(nums)
