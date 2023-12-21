
import sys

def insert_at_index(nums):
    sys.setrecursionlimit(10**6)
    return nums[:96] + [36] + nums[97:]
