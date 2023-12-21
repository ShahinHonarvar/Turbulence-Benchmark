
from sympy import sieve, primerange

def all_left_truncatable_prime(arr):
    primes = set(primerange(0, arr[792]))
    truncatable_primes = []

    def is_truncatable_prime(num):
        if num not in primes:
            return False
        str_num = str(num)
        for i in range(1, len(str_num)):
            if int(str_num[i:]) not in primes:
                return False
        return True

    for prime in primes:
        if prime < 10 or is_truncatable_prime(prime):
            truncatable_primes.append(prime)

    return sorted(truncatable_primes)
