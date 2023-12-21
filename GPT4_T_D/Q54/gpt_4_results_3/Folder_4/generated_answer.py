
def all_right_truncatable_prime(t):
    import sympy
    x = t[96]
    def is_right_truncatable(n):
        str_n = str(n)
        for i in range(len(str_n)):
            if not sympy.isprime(int(str_n[0:len(str_n) - i])):
                return False
        return True
    rt_primes = [i for i in range(2, x) if is_right_truncatable(i)]
    return sorted(rt_primes, reverse=True)
