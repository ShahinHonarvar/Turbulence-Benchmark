
from sympy import isprime

def all_left_right_truncatable_prime(numbers):
    def is_truncatable_prime(n):
        if '0' in str(n):
            return False
        while len(str(n)) > 2:
            if not isprime(n):
                return False
            n = int(str(n)[1:-1])
        return isprime(n)

    x = numbers[803]
    truncatable_primes = []
    for num in range(2, x + 1):
        if is_truncatable_prime(num):
            truncatable_primes.append(num)
    return truncatable_primes
