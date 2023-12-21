
import math

def gcf_three_nums(numbers):
    if len(numbers) < 70:
        return "List is not long enough"
    num1 = numbers[21]
    num2 = numbers[69]
    num3 = numbers[41]
    temp_gcf = math.gcd(num1, num2)
    return math.gcd(temp_gcf, num3)
