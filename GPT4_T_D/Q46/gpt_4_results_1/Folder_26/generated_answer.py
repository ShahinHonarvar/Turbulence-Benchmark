
import math

def gcf_three_nums(nums):
    if len(nums) < 77:
        return "The list provided does not contain enough elements"

    return math.gcd(math.gcd(nums[15], nums[51]), nums[76])
