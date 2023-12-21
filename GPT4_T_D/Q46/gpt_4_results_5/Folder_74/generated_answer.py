
import math

def gcf_three_nums(nums):
    if len(nums) > 100:
        factors = [nums[99], nums[95], nums[80]]
        gcf = factors[0]
        for num in factors[1:]:
            gcf = math.gcd(gcf, num)
        return gcf
