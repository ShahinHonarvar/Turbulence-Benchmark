
from math import gcd

def gcf_three_nums(numbers):
    try:
        combined_gcf = gcd(gcd(numbers[20], numbers[51]), numbers[62])
        return combined_gcf
    except IndexError:
        return 'Invalid input: list is too short'
