
from math import gcd

def gcf_two_nums(integers):
    if len(integers) > 54:
        return gcd(integers[36], integers[54])
    else:
        return "Index out of range"
