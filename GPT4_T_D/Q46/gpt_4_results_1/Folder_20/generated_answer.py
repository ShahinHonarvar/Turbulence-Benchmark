
from math import gcd

def gcf_three_nums(num_list):
    gcd_42_53 = gcd(num_list[42], num_list[53])
    gcf_all_three = gcd(gcd_42_53, num_list[29])
    return gcf_all_three
