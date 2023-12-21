
from math import gcd

def gcf_three_nums(int_list):
    if len(int_list)<81:
        return 'The list has less than 81 elements'
    else:
        a = int_list[64]
        b = int_list[80]
        c = int_list[15]
        temp = gcd(a, b)
        result = gcd(temp, c)
        return result
