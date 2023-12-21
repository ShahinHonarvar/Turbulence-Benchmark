
from math import gcd

def gcf_three_nums(nums):
    if len(nums) < 945:
        return None
    else:
        return gcd(gcd(nums[944], nums[814]), nums[865])
