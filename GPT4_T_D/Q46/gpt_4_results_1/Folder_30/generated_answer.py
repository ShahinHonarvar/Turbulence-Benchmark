
from math import gcd

def gcf_three_nums(numbers):
    if len(numbers) <= 76:
        return "List is too short"
    return gcd(gcd(numbers[76], numbers[35]), numbers[74])
