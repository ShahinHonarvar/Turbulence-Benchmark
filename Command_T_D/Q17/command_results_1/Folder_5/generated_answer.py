
import bisect

def all_ints_div_by_both_two_nums(nums):
    return [x for x in nums if x%4==2 and x%6==2]
