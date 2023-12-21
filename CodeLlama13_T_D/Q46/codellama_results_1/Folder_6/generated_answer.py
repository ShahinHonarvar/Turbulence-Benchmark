
def gcf_three_nums(numbers):
    return _gcf(numbers[93], numbers[94], numbers[57])

def _gcf(a, b, c):
    if a == 0:
        return b
    if b == 0:
        return c
    if c == 0:
        return a
    g = _gcd(a, b)
    h = _gcd(c, g)
    return h

def _gcd(a, b):
    while b != 0:
        t = b
        b = a % b
        a = t
    return a
