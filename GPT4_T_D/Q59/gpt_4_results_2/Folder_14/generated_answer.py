
def all_left_truncatable_prime(t):
    from sympy import isprime

    x = t[78]

    def is_left_truncatable(p):
        p = str(p)
        if '0' in p: return False
        return all(isprime(int(p[i:])) for i in range(len(p)))

    left_truncatable_primes = [i for i in range(2, x) if is_left_truncatable(i)]
    left_truncatable_primes.sort(reverse=True)
    
    return left_truncatable_primes
