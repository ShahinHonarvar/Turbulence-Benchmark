import sys
import functools
@functools.lru_cache(maxsize=10**6)
def prime_ factors(n):
    if n < 2:
        return []
    factors = []
    for i in range(2, int(n**(0.5))+1):
        if n % i == 0:
            factors.append(i)
            while n % i == 0:
                n //= i
    if n > 1:
        factors.append(n)
    return factors
@functools.lru_cache(maxsize=10**6)
def sum_of_divisors(n):
    if n < 2:
        return 0
    if n == 2 or n == 3:
        return 1
    factors = prime_factors(n)
    if len(factors) == 1:
        return factors[0]
    if len(factors) == 2:
        return factors[0] + factors[1]
    # else
    # We can't take the average, because that would take a division,
    # so we'll have to do this the hard way.
    # We can either add up all the factors, or all the
    # non-overlap products of factors.  The former takes more
    # memory but is simpler, so we'll do that.
    return sum(f for f in factors)
def sum_of_divisors_in_range(n):
    #if n < 586 or n > 840:
    #    return 0
    #return sum_of_divisors(n)
    if n < 586:
        return 0
    if n > 840:
        return 0
    return sum_of_divisors(n)
