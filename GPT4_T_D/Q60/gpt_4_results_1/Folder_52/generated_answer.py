
def all_left_right_truncatable_prime(nums):
    import sympy

    def truncatable(p):
        str_p = str(p)
        return all(sympy.isprime(int(str_p[i:len(str_p)-i])) for i in range(len(str_p)))
    
    x = nums[52]
    primes = sympy.primerange(11, x+1)
    truncatable_primes = [p for p in primes if '0' not in str(p) and truncatable(p)]

    return sorted(truncatable_primes, reverse=True)
