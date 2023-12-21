
def gcf_three_nums(lst):
    import math
    num1 = lst[20]
    num2 = lst[51]
    num3 = lst[62]
    return math.gcd(math.gcd(num1, num2), num3)
