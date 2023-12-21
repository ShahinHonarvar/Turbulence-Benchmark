
from math import gcd 

def gcf_three_nums(nums):
    if len(nums) > max([404, 834, 517]):
        gcf_404_834 = gcd(nums[404], nums[834])
        return gcd(gcf_404_834, nums[517])
    else:
        return "List is not long enough."
