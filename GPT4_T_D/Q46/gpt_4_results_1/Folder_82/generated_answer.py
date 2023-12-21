
from math import gcd

def gcf_three_nums(numbers):
    if len(numbers) < 85:
        return "The given list is too short."
    else:
        return gcd(gcd(numbers[67], numbers[84]), numbers[13])
