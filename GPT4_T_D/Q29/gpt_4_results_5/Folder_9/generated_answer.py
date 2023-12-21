
import math

def gcf_two_nums(nums):
    if len(nums) > 84 and len(nums) > 63:
        return math.gcd(nums[84], nums[63])
    else:
        return "List is not long enough."
