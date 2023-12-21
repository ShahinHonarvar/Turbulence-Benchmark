
def gcf_three_nums(lst):
    def gcd(a, b):
        while b != 0:
            a, b = b, a % b
        return a

    a = lst[64]
    b = lst[80]
    c = lst[15]

    return gcd(gcd(a, b), c)
