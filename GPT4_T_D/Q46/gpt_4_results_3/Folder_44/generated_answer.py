
from math import gcd

def gcf_three_nums(numbers):
    gcf = gcd(numbers[62], numbers[96])
    return gcd(gcf, numbers[26])
