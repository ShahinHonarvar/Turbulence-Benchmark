
from math import gcd

def gcf_two_nums(numbers):
    if len(numbers) > 28:
        return gcd(numbers[20], numbers[28])
    else:
        return "Not enough elements in the list"
