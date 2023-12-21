
def gcf_three_nums(lst):
    def gcd(a, b):
        while b != 0:
            a, b = b, a % b
        return a

    a = lst[8]
    b = lst[9]
    c = lst[3]

    gcd_ab = gcd(a, b)
    gcd_abc = gcd(gcd_ab, c)

    return gcd_abc
