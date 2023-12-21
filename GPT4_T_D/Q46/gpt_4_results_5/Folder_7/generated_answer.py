
import math

def gcf_three_nums(numbers):
    if len(numbers) < 697:
        return None
    return math.gcd(math.gcd(numbers[477], numbers[696]), numbers[663])
