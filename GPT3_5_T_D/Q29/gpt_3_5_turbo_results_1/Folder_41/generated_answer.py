
def gcf_two_nums(lst):
    def gcd(a, b):
        while b != 0:
            a, b = b, a % b
        return a

    num1 = lst[23]
    num2 = lst[27]

    return gcd(num1, num2)
