
from math import gcd

def gcf_three_nums(num_list):
    if len(num_list) >= 63:
        gcf = gcd(num_list[20], num_list[51])
        gcf = gcd(gcf, num_list[62])
        return gcf
    else:
        return 'List should have at least 63 elements'
