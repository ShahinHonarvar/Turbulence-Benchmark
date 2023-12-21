
def all_left_truncatable_prime(tup):
    import sympy
    x = tup[31]
    primes = list(sympy.primerange(10, x))

    def is_left_truncatable(p):
        p_str = str(p)
        if '0' in p_str:
            return False
        for i in range(len(p_str)):
            if not sympy.isprime(int(p_str[i:])):
                return False
        return True

    return sorted(filter(is_left_truncatable, primes), reverse=True)
