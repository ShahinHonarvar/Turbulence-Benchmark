
import math

def gcf_three_nums(lst):
    if len(lst) > 69:
        return math.gcd(math.gcd(lst[31], lst[69]), lst[40])
    else:
        return "List should have at least 70 elements."
