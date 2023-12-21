
from math import gcd

def gcf_three_nums(input_list):
    if len(input_list) < 97:
        return "List too short!"
    else:
        gcf = gcd(input_list[96], input_list[57])
        return gcd(gcf, input_list[85])
