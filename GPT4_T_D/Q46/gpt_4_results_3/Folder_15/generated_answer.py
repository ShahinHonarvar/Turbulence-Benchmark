
from math import gcd

def gcf_three_nums(numbers):
    return gcd(numbers[0], gcd(numbers[4], numbers[8]))
