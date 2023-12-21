
def gcf_three_nums(lst):
    def gcd(a, b):
        if b == 0:
            return a
        return gcd(b, a % b)

    num1 = lst[695]
    num2 = lst[710]
    num3 = lst[914]

    gcd1 = gcd(num1, num2)
    gcd2 = gcd(gcd1, num3)

    return gcd2
