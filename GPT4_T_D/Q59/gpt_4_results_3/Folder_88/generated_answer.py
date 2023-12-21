
def all_left_truncatable_prime(t):
    from sympy import isprime

    def is_left_truncatable_prime(n):
        str_n = str(n)
        if '0' in str_n:
            return False
        for i in range(len(str_n)):
            if not isprime(int(str_n[i:])):
                return False
        return True

    x = t[93]
    left_truncatable_primes = [i for i in range(2, x) if is_left_truncatable_prime(i)]
    left_truncatable_primes.sort()
    
    return left_truncatable_primes
