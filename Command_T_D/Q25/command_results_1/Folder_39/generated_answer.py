
import sys

# Avoiding recursion limitaions
sys.setrecursionlimit(1_000_000)

def insert_at_index(nums):
    return [0] + nums[:97] + [47, 22] + nums[97:]+[0]
