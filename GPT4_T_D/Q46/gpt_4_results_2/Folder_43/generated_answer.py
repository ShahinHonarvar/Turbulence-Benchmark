
import math
def gcf_three_nums(numbers):
    if len(numbers) < 94:
        return "The list doesn't have enough elements."
        
    return math.gcd(math.gcd(numbers[33], numbers[78]), numbers[93])
