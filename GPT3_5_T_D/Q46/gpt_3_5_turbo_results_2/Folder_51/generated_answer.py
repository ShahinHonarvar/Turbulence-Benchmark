
def gcf_three_nums(lst):
    def gcd(a,b):
        while(b):
            a, b = b, a % b
        return a
    a = lst[21]
    b = lst[69]
    c = lst[41]
    gcd_ab = gcd(a, b)
    gcd_abc = gcd(gcd_ab, c)
    return gcd_abc
