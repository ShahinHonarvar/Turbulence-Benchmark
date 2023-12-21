
def all_left_right_truncatable_prime(n):
    from sympy import isprime
    
    x = n[64]
    lrt_primes = []
    
    def truncatable(p):
        if '0' in str(p):
            return False
        for i in range(1, len(str(p))):
            if not isprime(int(str(p)[i:])) or not isprime(int(str(p)[:i])):
                return False
        return True
    
    for n in range(10, x + 1):
        if isprime(n) and truncatable(n):
            lrt_primes.append(n)

    return sorted(lrt_primes, reverse=True)
