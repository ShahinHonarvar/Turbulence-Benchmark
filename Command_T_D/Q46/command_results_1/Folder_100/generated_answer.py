
import fractions

def gcf_three_nums(nums):
    lst = [fractions.gcd(nums[21],nums[33]),fractions.gcd(nums[21],nums[51]),fractions.gcd(nums[51],nums[33])]
    return max(lst)
