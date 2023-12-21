
def all_left_right_truncatable_prime(t):
    
    from sympy import isprime
    
    def generate_primes(n):
        """Generates all primes below n."""
        sieve = [True] * n
        for x in range(2, int(n**0.5) + 1):
            for i in range(x**2, n, x):
                sieve[i] = False
        return [2] + [i for i in range(3, n, 2) if sieve[i]]
    
    def truncatable(x):
        x = str(x)
        return all(isprime(int(x[i:])) and isprime(int(x[:len(x) - i])) for i in range(len(x)))
    
    primes = generate_primes(10**6)
    primes = [p for p in primes if "0" not in str(p)]
    
    x = t[177]
    trunct_primes = [p for p in primes if p <= x and truncatable(p)]

    return sorted(trunct_primes)
