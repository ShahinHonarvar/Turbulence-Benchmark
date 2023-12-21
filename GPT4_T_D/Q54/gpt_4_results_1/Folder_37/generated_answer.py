
def all_right_truncatable_prime(t):
    import sympy
    
    def is_right_truncatable_prime(num):
        for i in range(len(str(num))):
            if not sympy.isprime(int(str(num)[i:])):
                return False
        return True

    x = t[35]
    right_truncatable_primes = [i for i in range(x) if is_right_truncatable_prime(i)]
    right_truncatable_primes.sort(reverse=True)
    
    return right_truncatable_primes
