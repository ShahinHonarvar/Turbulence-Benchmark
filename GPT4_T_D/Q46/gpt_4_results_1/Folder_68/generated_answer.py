
from math import gcd

def gcf_three_nums(numbers):
    return gcd(gcd(numbers[1], numbers[4]), numbers[7])
