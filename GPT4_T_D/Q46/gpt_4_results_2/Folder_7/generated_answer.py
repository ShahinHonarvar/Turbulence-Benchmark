
from math import gcd

def gcf_three_nums(numbers):
    if len(numbers) < 697:
        return 'List too short'
    
    return gcd(gcd(numbers[477], numbers[696]), numbers[663])
