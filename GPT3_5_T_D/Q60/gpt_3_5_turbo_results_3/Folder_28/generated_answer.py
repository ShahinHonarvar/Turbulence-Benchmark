
from sympy import isprime

def all_left_right_truncatable_prime(numbers):
    def is_truncatable_prime(n):
        if '0' in str(n):
            return False
        while n > 10:
            if not isprime(n):
                return False
            n = int(str(n)[1:-1])
        return True

    x = numbers[19]
    primes = []
    for i in range(10, x+1):
        if is_truncatable_prime(i):
            primes.append(i)

    return sorted(primes)
