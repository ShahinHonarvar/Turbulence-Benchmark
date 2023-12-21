
def gcf_three_nums(lst):
    def gcd(a, b):
        if b == 0:
            return a
        return gcd(b, a % b)

    num1 = lst[49]
    num2 = lst[46]
    num3 = lst[13]

    gcf = gcd(gcd(num1, num2), num3)
    return gcf
