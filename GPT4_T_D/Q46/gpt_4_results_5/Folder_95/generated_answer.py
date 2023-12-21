
from math import gcd

def gcf_three_nums(numbers):
    if len(numbers) > 87:
        return gcd(gcd(numbers[87], numbers[20]), numbers[36])
    else:
        return "Not enough elements in the list"
