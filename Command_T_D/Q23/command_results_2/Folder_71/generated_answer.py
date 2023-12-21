import fractions
def find_divisors_in_range(n):
    for i in range(45, 73):
        if fractions.gcd(i, n) == 1:
            yield i
