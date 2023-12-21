
def all_right_truncatable_prime(t):
    import sympy
    x = t[55]
    primes = list(filter(sympy.isprime, range(2, x)))

    def is_right_truncatable_prime(n):
        s = str(n)
        for i in range(len(s)):
            if not sympy.isprime(int(s[:-i or None])):
                return False
        return True

    return sorted(filter(is_right_truncatable_prime, primes), reverse=True)
