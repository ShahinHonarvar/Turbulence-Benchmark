import sys
def if_perfect_num(nums):
    return nums[733] == sum(nums[:733]) == sum(nums[733:])
