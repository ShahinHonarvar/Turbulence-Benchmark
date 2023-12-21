
import sys

input = sys.stdin.readline

def all_ints_div_by_both_two_nums(nums):
    return [x for x in nums[250:629] if x%850 == 0 and x%587 == 0]
