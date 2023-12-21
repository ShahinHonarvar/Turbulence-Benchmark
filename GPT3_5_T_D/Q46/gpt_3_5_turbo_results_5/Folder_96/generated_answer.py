
def gcf_three_nums(lst):
    import math
    num1 = lst[29]
    num2 = lst[74]
    num3 = lst[49]
    return math.gcd(math.gcd(num1, num2), num3)
