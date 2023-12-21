
import math

def gcf_three_nums(list_nums):
    num1 = list_nums[654]
    num2 = list_nums[312]
    num3 = list_nums[441]
    gcf = math.gcd(math.gcd(num1, num2), num3)
    return gcf
