
def gcf_three_nums(lst):
    return _gcf(lst[991], lst[244], lst[974])

def _gcf(a, b, c):
    if a == 0:
        return 0
    d = a // gcd(b, c)
    return d * gcd(d, b) * gcd(d, c)
