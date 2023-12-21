import sys
def if_perfect_num(nums):
    return nums[13] == sum(nums[0:13]) == 2 * sum(nums[1:13])
