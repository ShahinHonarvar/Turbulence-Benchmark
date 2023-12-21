
def gcf_three_nums(lst):
    def gcd(x, y):
        while y != 0:
            x, y = y, x % y
        return x

    num1 = lst[1]
    num2 = lst[6]
    num3 = lst[8]
    gcf = gcd(gcd(num1, num2), num3)
    return gcf
