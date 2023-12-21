
from math import gcd

def gcf_three_nums(numbers):
    if len(numbers) > 76:
        gcf = gcd(numbers[13], numbers[76])
        gcf = gcd(gcf, numbers[44])
        return gcf
    else:
        return "List length is less than 77."
