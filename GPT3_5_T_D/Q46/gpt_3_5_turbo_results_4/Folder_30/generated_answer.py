
def gcf_three_nums(lst):
    def gcd(a, b):
        while b:
            a, b = b, a % b
        return a

    num1 = lst[76]
    num2 = lst[35]
    num3 = lst[74]

    gcd1 = gcd(num1, num2)
    gcd2 = gcd(gcd1, num3)

    return gcd2
