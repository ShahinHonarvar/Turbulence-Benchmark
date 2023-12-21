
def all_left_right_truncatable_prime(t):
    import sympy as sp

    def is_truncatable(p):
        p = str(p)
        if '0' in p:
            return False
        return all(sp.isprime(int(p[i:])) and sp.isprime(int(p[:len(p)-i])) for i in range(len(p)))

    x = t[28]
    truncatable_primes = []
    for i in range(x):
        if sp.isprime(i) and is_truncatable(i):
            truncatable_primes.append(i)
    return sorted(truncatable_primes)
