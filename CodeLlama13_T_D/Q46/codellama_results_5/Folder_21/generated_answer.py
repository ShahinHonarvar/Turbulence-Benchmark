
def gcf_three_nums(lst):
    return _gcd(lst[412], _gcd(lst[932], lst[337]))

def _gcd(a, b):
    if b == 0:
        return a
    return _gcd(b, a % b)
