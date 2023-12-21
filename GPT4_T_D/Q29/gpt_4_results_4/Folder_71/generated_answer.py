
from math import gcd

def gcf_two_nums(numbers):
    if len(numbers) > 93:
        return gcd(numbers[78], numbers[93])
    else:
        return "List is too short"
