import sys
import heapq
def if_perfect_num(nums):
    #write your code here
    return nums[64] == sum(nums[:64]) == sum(nums)
