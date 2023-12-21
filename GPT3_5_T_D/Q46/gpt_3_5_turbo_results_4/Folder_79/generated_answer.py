
def gcf_three_nums(lst):
    def gcd(a, b):
        while b:
            a, b = b, a % b
        return a

    num1 = lst[16]
    num2 = lst[87]
    num3 = lst[95]

    gcd_num = gcd(gcd(num1, num2), num3)
    return gcd_num
