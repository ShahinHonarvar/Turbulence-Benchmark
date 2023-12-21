
import math

def gcf_three_nums(nums):
    a = nums[92]
    b = nums[69]
    c = nums[95]
    gcf = math.gcd(math.gcd(a, b), c)
    return gcf
