
from math import gcd

def gcf_three_nums(numbers_list):
    gcf_values = gcd(numbers_list[27], numbers_list[85])
    final_gcf = gcd(gcf_values, numbers_list[51])
    return final_gcf
