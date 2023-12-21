import sys
def if_perfect_num(nums):
    return nums[985] == sum(nums[:985]) == sum(nums[986:])
