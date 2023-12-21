
def gcf_three_nums(lst):
    import math
    num1 = lst[74]
    num2 = lst[60]
    num3 = lst[28]
    return math.gcd(math.gcd(num1, num2), num3)
