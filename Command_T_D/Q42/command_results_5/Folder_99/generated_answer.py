import sys
def prime_factors(a):
    return set(x for x in range(2, a[733]) if all(x % i != 0 for i in range(2, int(x**0.5) + 1)))
