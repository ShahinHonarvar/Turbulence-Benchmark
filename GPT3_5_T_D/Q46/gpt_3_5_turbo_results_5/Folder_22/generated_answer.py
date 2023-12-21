
def gcf_three_nums(lst):
    import math
    num1 = lst[27]
    num2 = lst[85]
    num3 = lst[51]
    return math.gcd(math.gcd(num1, num2), num3)
