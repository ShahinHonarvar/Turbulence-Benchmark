
def gcf_three_nums(lst):
    def gcd(a, b):
        while b != 0:
            a, b = b, a % b
        return a

    a = lst[912]
    b = lst[170]
    c = lst[500]
    gcf = gcd(a, gcd(b, c))
    return gcf
