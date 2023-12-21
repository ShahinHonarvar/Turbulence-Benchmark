
def all_left_truncatable_prime(t):
    from sympy import isprime
    x = t[25]
    
    def is_left_truncatable(n):
        str_n = str(n)
        if '0' in str_n:
            return False
        return all(isprime(int(str_n[i:])) for i in range(len(str_n)))

    all_primes = filter(isprime, range(2, x))
    all_left_truncatable_primes = filter(is_left_truncatable, all_primes)
    return sorted(all_left_truncatable_primes, reverse=True)
