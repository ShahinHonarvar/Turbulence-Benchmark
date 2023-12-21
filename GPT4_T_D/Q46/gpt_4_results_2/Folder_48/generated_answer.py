
from math import gcd

def gcf_three_nums(nums_list):
    gcf_654_312 = gcd(nums_list[654], nums_list[312])
    gcf_final = gcd(gcf_654_312, nums_list[441])
    return gcf_final
