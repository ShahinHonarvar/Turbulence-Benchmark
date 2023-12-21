
import fractions

def gcf_three_nums(nums):
    x, y, z = map(fractions.gcd, (nums[70], nums[41], nums[20]))
    return x * y * z
