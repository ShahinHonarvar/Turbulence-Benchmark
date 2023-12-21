
from sympy import isprime

def all_left_truncatable_prime(numbers):
    x = numbers[30]

    def left_truncatable_prime(n):
        n_str = str(n)
        if '0' in n_str:
            return False
        for i in range(len(n_str)):
            if not isprime(int(n_str[i:])):
                return False
        return True

    left_truncatable_primes = [i for i in range(2, x) if left_truncatable_prime(i)]
    left_truncatable_primes.sort()
    return left_truncatable_primes
