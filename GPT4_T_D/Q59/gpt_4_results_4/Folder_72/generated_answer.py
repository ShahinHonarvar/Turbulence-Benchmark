
from sympy import isprime

def all_left_truncatable_prime(t):
    x = t[31]

    def is_left_truncatable_prime(n):
        num_str = str(n)
        if '0' in num_str:
            return False
        for j in range(len(num_str)):
            if not isprime(int(num_str[j:])):
                return False
        return True

    left_truncatable_primes = [num for num in range(2, x) if is_left_truncatable_prime(num)]
    left_truncatable_primes.sort(reverse=True)
    return left_truncatable_primes
