
import math

def gcf_two_nums(nums):
    if len(nums) > 88 and len(nums) > 35:
        return math.gcd(nums[88], nums[35])
    else:
        return "List is too short"
