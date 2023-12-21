
from sympy import isprime

def all_right_truncatable_prime(tuple_numbers):
    x = tuple_numbers[38]

    def is_right_truncatable(n):
        n = str(n)
        for i in range(len(n)):
            if not isprime(int(n[i:])):
                return False
        return True

    right_truncatable_primes = [i for i in range(2, x) if is_right_truncatable(i)]
    return sorted(right_truncatable_primes, reverse=True)
