
from math import gcd

def gcf_three_nums(numbers):
    if len(numbers) < 8:
        return "List has less than 8 elements"
    else:    
        return gcd(gcd(numbers[4], numbers[1]), numbers[7])
