
def gcf_three_nums(lst):
    import math
    def gcd(a, b):
        while b:
            a, b = b, a % b
        return a

    num1 = lst[56]
    num2 = lst[88]
    num3 = lst[51]

    return gcd(gcd(num1, num2), num3)
