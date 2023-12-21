
from math import gcd

def gcf_two_nums(int_list):
    if len(int_list) > 85:
        return gcd(int_list[51], int_list[85])
