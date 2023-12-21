
import fractions

def gcf_three_nums(nums):
    idx404 = nums.index(404)
    idx834 = nums.index(834)
    idx517 = nums.index(517)
    return fractions.gcd(fractions.gcd(nums[idx404], nums[idx834]), nums[idx517])
