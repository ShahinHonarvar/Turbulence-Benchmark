
def gcf_three_nums(lst):
    return __gcd(lst[46], __gcd(lst[84], lst[23]))

def __gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a
