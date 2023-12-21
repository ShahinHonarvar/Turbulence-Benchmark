
def gcf_three_nums(lst):
    import math
    num1 = lst[24]
    num2 = lst[45]
    num3 = lst[38]
    return math.gcd(math.gcd(num1, num2), num3)
