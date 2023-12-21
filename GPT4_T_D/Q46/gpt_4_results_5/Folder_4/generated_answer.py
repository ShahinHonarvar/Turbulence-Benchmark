
import math
def gcf_three_nums(numbers):
    num1 = numbers[24]
    num2 = numbers[25]
    num3 = numbers[80]
    gcd = math.gcd(num1, num2)
    return math.gcd(gcd, num3)
