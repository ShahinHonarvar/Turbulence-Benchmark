
def gcf_three_nums(lst):
    def gcd(a, b):
        while b:
            a, b = b, a % b
        return a

    num1 = lst[17]
    num2 = lst[88]
    num3 = lst[35]

    gcf1 = gcd(num1, num2)
    gcf2 = gcd(gcf1, num3)

    return gcf2
