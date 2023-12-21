
def gcf_three_nums(lst):
    def gcd(a, b):
        while b:
            a, b = b, a % b
        return a

    num1 = lst[20]
    num2 = lst[43]
    num3 = lst[95]

    gcf1 = gcd(num1, num2)
    gcf2 = gcd(gcf1, num3)

    return gcf2
