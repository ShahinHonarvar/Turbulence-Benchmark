
from sympy import primerange, isprime

def all_left_truncatable_prime(numbers):
    def is_left_truncatable(p):
        if '0' in p:
            return False
        else:
            for i in range(len(p)):
                if not isprime(int(p[i:])):
                    return False
            return True
    
    x = numbers[630]
    primes = list(primerange(10, x))
    left_truncatable_primes = [p for p in primes if is_left_truncatable(str(p))]

    return sorted(left_truncatable_primes, reverse=True)
