
def gcf_three_nums(lst):
    def gcd(a, b):
        while b:
            a, b = b, a % b
        return a

    num1 = lst[44]
    num2 = lst[91]
    num3 = lst[42]

    gcf = gcd(num1, gcd(num2, num3))

    return gcf
