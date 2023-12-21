
from math import gcd

def gcf_three_nums(lst):
    if len(lst) > 62:
        num1 = lst[20]
        num2 = lst[51]
        num3 = lst[62]
        return gcd(gcd(num1, num2), num3)
    else:
        return "List is too short."
