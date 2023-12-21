
def all_left_truncatable_prime(t):
    from sympy import isprime
    x = t[86]

    def is_left_prime(n):
        if '0' in str(n): return False
        for i in range(1, len(str(n))):
            trunc_n = int(str(n)[i:])
            if not isprime(trunc_n): return False
        return True
        
    return sorted(filter(lambda p: isprime(p) and is_left_prime(p), range(2, x)))
