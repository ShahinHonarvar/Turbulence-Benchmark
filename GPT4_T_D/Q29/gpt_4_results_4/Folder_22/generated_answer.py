
import math

def gcf_two_nums(nums):
    if len(nums) <= 68:
        raise ValueError("List must contain at least 69 elements")

    return math.gcd(nums[24], nums[68])
