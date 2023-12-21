
import math

def gcf_two_nums(numbers):
    if len(numbers) > 49 and len(numbers) > 31:
        num1 = numbers[49]
        num2 = numbers[31]
        return math.gcd(num1, num2)
    else:
        return "The list is not long enough"
