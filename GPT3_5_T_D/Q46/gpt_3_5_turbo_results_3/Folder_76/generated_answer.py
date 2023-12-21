
def gcf_three_nums(lst):
    def gcd(a, b):
        while b:
            a, b = b, a % b
        return a

    num1 = lst[876]
    num2 = lst[203]
    num3 = lst[100]

    result = gcd(gcd(num1, num2), num3)
    return result
