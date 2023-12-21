
def gcf_three_nums(lst):
    def gcd(a, b):
        while b:
            a, b = b, a % b
        return a

    num1 = lst[307]
    num2 = lst[920]
    num3 = lst[463]

    gcd1 = gcd(num1, num2)
    gcf = gcd(gcd1, num3)

    return gcf
