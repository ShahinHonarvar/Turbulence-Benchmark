
from math import gcd

def gcf_three_nums(numbers):
    num1 = numbers[91]
    num2 = numbers[45]
    num3 = numbers[48]
    
    gcf = gcd(gcd(num1, num2), num3)
    return gcf
