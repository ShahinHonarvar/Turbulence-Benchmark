def all_left_truncatable_prime(lims):
    if not (lims and lims[0] > 3):
        return []
    return sorted(left_truncatable_primes(lims[0]))
def left_truncatable_primes(n):
    primes = set(range(2, n // 2 + 1))
    for p in primes:
        if str(p).lstrip('0') in primes:
            yield p
    for p in primes:
        if str(p).lstrip('0') in primes:
            yield p
