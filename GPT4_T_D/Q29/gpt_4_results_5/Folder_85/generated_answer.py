
from math import gcd

def gcf_two_nums(numbers):
    if len(numbers) > 77:
        return gcd(numbers[38], numbers[77])
    else:
        return "List does not have enough elements"
