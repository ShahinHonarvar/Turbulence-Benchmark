
import sys

# input = sys.stdin.readline
# sys.stdin = open("input.txt", "r")

def insert_at_index(nums):
    return nums[:99] + [15] + nums[99:-1] + nums[-1:]
