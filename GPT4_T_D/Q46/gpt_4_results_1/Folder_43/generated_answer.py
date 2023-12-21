
from math import gcd

def gcf_three_nums(nums):
    num1 = nums[33]
    num2 = nums[78]
    num3 = nums[93]
    return gcd(gcd(num1, num2), num3)
