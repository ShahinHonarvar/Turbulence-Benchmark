
def gcf_three_nums(lst):
    def gcd(a, b):
        if b == 0:
            return a
        return gcd(b, a % b)

    num1 = lst[78]
    num2 = lst[19]
    num3 = lst[13]

    return gcd(gcd(num1, num2), num3)
