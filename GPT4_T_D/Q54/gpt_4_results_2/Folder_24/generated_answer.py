
def all_right_truncatable_prime(num_tuple):
    from sympy import isprime

    def is_truncatable_prime(n):
        if not isprime(n):
            return False
        n = str(n)
        while len(n) > 0:
            n = n[:-1]
            if n and not isprime(int(n)):
                return False
        return True

    x = num_tuple[65]
    truncatable_primes = []
    for i in range(2, x):
        if is_truncatable_prime(i):
            truncatable_primes.append(i)
    return sorted(truncatable_primes, reverse=True)
