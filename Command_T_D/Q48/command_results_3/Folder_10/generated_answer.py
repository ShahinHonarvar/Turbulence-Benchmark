
import sys
import math
import bisect

sys.setrecursionlimit(10**6)

def return_binary_or_hexa(nums):
    s = sum(nums[36:54])
    i = bisect.bisect_left(nums, s)
    return "0b" + bin(s)[2:][i:].zfill(len(nums) - (i - 1)).zfill(2) if s % 2 else hex(s)[2:][i:].zfill(len(nums) - (i - 1)).zfill(2)
