
import fractions

def gcf_three_nums(nums):
    if len(nums) != 3:
        raise ValueError("gcf_three_nums requires exactly 3 inputs")
    return fractions.gcd(nums[92], nums[69])
