
import math

def gcf_two_nums(num_list):
    if len(num_list) >= 54:
        return math.gcd(num_list[29], num_list[53])
    else:
        return "List is not long enough"
