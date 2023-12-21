
def all_left_right_truncatable_prime(tup):
    import sympy

    def is_truncatable(p):
        p_str = str(p)
        if '0' in p_str:
            return False
        for i in range(1, len(p_str)):
            left = int(p_str[i:])
            right = int(p_str[:i])
            if not sympy.isprime(left) or not sympy.isprime(right):
                return False
        return True
    
    x = tup[645]
    truncatable_primes = []

    for val in sympy.primerange(10, x+1):
        if is_truncatable(val):
            truncatable_primes.append(val)
            
    return truncatable_primes
