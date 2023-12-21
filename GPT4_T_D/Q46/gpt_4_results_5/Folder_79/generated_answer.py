
import math

def gcf_three_nums(lst):
    if len(lst) < 96:
        return "List is too short. Please pass a list with at least 96 elements."
    else:
        return math.gcd(math.gcd(lst[16], lst[87]), lst[95])
