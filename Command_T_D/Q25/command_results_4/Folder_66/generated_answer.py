
import sys

sys.setrecursionlimit(10**6)

def insert_at_index(nums):
    return nums[:62] + [19, 13] + nums[62:-1] + nums[-1:]
