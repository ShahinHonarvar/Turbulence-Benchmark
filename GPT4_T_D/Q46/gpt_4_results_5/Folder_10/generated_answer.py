
from math import gcd

def gcf_three_nums(nums):
    first = nums[86]
    second = nums[89]
    third = nums[49]
    
    temp = gcd(first,second)
    return gcd(temp,third)
