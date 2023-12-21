
from math import gcd

def gcf_three_nums(numbers):
    if len(numbers) < 70:
        raise ValueError('List must contain at least 70 elements')
    else:
        result = gcd(numbers[31], numbers[69])
        result = gcd(result, numbers[40])
        return result
