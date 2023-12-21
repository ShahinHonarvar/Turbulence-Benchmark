
import math

def prime_factors(lst):
    value = lst[537]
    factors = set()

    for i in range(2, math.isqrt(value) + 1):
        while value % i == 0:
            factors.add(i)
            value = value // i

    if value > 1:
        factors.add(value)

    return factors
