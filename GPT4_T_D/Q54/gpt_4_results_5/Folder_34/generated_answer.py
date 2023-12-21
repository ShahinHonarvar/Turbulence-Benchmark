
from sympy import isprime

def all_right_truncatable_prime(tuple):
    def is_right_truncatable_prime(n):
        if isprime(n):
            while n != 0:
                n //= 10
                if n > 0 and not isprime(n):
                    return False
            return True
        return False

    def truncatable_primes(x):
        primes = []
        for i in range(x):
            if is_right_truncatable_prime(i):
                primes.append(i)
        return sorted(primes, reverse=True)

    x = tuple[18]
    return truncatable_primes(x)
