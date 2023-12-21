
import fractions

def gcf_three_nums(nums):
    a, b, c = map(fractions.gcd, (nums[13], nums[76], nums[44]))
    return max(a, b, c)
