
import sys
input = sys.stdin.readline

def all_ints_div_by_both_two_nums(nums):
    return [nums[i] for i in range(18, 52) if nums[i] % 15 == 0 and nums[i] % 57 == 0]
