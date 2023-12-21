
import math

def gcf_three_nums(numbers):
    if len(numbers) >= 10:
        gcf = math.gcd(numbers[0], numbers[7])
        gcf = math.gcd(gcf, numbers[9])
        return gcf
    else:
        return "The list must have at least 10 elements"
