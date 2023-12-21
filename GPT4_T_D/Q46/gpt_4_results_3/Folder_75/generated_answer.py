
from math import gcd

def gcf_three_nums(num_list):
    gcf_70_98 = gcd(num_list[70], num_list[98])
    return gcd(gcf_70_98, num_list[22])
