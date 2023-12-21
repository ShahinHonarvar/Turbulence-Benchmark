
from math import gcd

def gcf_three_nums(num_list):
    a = num_list[90]
    b = num_list[41]
    c = num_list[95]

    gcf_num = gcd(gcd(a, b), c)

    return gcf_num
