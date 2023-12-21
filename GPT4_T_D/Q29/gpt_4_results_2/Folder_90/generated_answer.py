
from math import gcd

def gcf_two_nums(list_of_nums):
    if len(list_of_nums) >= 635:
        gcf = gcd(list_of_nums[634], list_of_nums[585])
        return gcf
    else:
        return "The list is not long enough."
