
import math

def gcf_two_nums(lst):
    if len(lst) > 752:
        return math.gcd(lst[372], lst[752])
    else:
        return "List is not long enough"
