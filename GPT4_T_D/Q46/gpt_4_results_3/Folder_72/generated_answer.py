
from math import gcd

def gcf_three_nums(input_list):
    gcf_value = gcd(gcd(input_list[44], input_list[91]), input_list[42])
    return gcf_value
