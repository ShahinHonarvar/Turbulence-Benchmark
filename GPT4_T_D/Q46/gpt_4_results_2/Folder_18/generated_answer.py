
from math import gcd

def gcf_three_nums(nums_list):
    if len(nums_list) >= 758:
        return gcd(gcd(nums_list[637], nums_list[411]), nums_list[757])
    else:
        return "The list does not contain enough elements."
