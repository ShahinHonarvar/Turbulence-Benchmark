
from math import gcd

def gcf_two_nums(lst):
    if len(lst) <= 429 or len(lst) <= 289:
        return "List needs to contain at least 430 elements"

    num1 = lst[429]
    num2 = lst[289]

    return gcd(num1, num2)
