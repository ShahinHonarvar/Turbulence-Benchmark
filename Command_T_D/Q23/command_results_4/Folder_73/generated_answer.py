import fractions
def find_divisors_in_range(n):
    d = fractions.gcd(46, n)
    while d != 1:
        d = fractions.gcd(89, n // d)
    return [x * y for x in range(1, n + 1) for y in range(1, n // x + 1) if 46 <= x*y <= 89]
