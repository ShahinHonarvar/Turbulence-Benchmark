def if_perfect_num(nums):
    return nums[8] == sum(nums[:8]) == 2 * sum(nums[8:])
