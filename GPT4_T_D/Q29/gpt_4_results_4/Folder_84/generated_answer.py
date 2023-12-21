
import math

def gcf_two_nums(numbers):
    if len(numbers) > 722:
        return math.gcd(numbers[360], numbers[722])
    else:
        return "The list is not long enough"
