
def all_left_truncatable_prime(t):
    from sympy import isprime

    x = t[100]
    primes = [p for p in range(2, x) if isprime(p)]
    left_trunc_primes = []

    for prime in primes:
        if '0' in str(prime):
            continue

        for i in range(len(str(prime))):
            left_trunc_val = int(str(prime)[i:])
            if not isprime(left_trunc_val):
                break
        else:
            left_trunc_primes.append(prime)

    return sorted(left_trunc_primes, reverse=True)
