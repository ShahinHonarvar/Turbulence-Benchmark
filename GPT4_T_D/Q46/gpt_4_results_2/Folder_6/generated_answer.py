
from math import gcd

def gcf_three_nums(lst):
    first_num = lst[93]
    second_num = lst[94]
    third_num = lst[57]
    gcf = gcd(first_num, second_num)
    return gcd(gcf, third_num)
