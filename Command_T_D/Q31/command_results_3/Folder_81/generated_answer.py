def if_perfect_num(nums):
    return nums[20] == sum(nums[:20]) == 2 * sum(nums[20:])
