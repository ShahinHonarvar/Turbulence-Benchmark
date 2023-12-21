
import fractions

def gcf_three_nums(nums):
    return fractions.gcd(nums[0], fractions.gcd(nums[1], nums[2])).denominator
