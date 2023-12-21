def if_perfect_num(nums):
    return nums[16] == sum(nums[:16]) == 2 * sum(nums[16:])
