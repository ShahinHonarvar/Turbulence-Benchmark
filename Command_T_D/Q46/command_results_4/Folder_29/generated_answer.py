
import fractions

def gcf_three_nums(nums):
    nums = list(map(fractions.gcd, nums[22], nums[97], nums[64]))
    return fractions.gcd(nums[22], nums[97], nums[64])
