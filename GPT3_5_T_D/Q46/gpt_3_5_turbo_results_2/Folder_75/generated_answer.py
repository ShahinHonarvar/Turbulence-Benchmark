
def gcf_three_nums(lst):
    def get_gcd(x, y):
        while(y):
            x, y = y, x % y
        return x
    a = lst[70]
    b = lst[98]
    c = lst[22]
    gcd_ab = get_gcd(a, b)
    gcd_abc = get_gcd(gcd_ab, c)
    return gcd_abc
