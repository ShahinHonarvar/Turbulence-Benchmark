
def gcf_three_nums(lst):
    def gcd(a, b):
        if a == 0:
            return b
        return gcd(b % a, a)

    a = lst[66]
    b = lst[90]
    c = lst[27]

    gcf_ab = gcd(a, b)
    gcf_abc = gcd(gcf_ab, c)

    return gcf_abc
