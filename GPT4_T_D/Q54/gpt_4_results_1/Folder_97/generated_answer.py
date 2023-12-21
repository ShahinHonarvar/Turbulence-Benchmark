
def all_right_truncatable_prime(t):
    from sympy import isprime
    
    def is_right_truncatable_prime(num):
        while num != 0:
            if not isprime(num):
                return False
            num = num // 10
        return True
    
    truncatable_primes = []
    x = t[645]
    for i in range(2, x):
        if is_right_truncatable_prime(i):
            truncatable_primes.append(i)
    return sorted(truncatable_primes)
