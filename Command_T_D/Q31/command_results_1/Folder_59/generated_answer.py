def if_perfect_num(nums):
    return nums[2] == sum(nums[0:-2]) == 2 * nums[1]
