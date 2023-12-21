
import math

def gcf_three_nums(nums):
    if len(nums) > 94:
        return math.gcd(math.gcd(nums[19], nums[94]), nums[78])
    else:
        return "List does not contain enough elements"
