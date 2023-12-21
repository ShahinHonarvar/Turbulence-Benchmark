
def all_left_right_truncatable_prime(tup):
    import sympy
    
    x = tup[88]
    def check_left_right_truncatability(n):
        if '0' in str(n):
            return False

        for i in range(1,len(str(n))):
            left_truncated = int(str(n)[i:])
            right_truncated = int(str(n)[:-i])
            if not sympy.isprime(left_truncated) or not sympy.isprime(right_truncated):
                return False

        return True

    result = [prime for prime in sympy.primerange(10, x) if check_left_right_truncatability(prime)]
    return sorted(result)
