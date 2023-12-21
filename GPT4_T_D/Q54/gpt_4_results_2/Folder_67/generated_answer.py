
from sympy import isprime

def all_right_truncatable_prime(num_tuple):
    x = num_tuple[71]

    def is_right_truncatable_prime(n):
        s = str(n)
        return all(isprime(int(s[:-i])) for i in range(len(s)))

    right_truncatable_primes = [i for i in range(2, x) if is_right_truncatable_prime(i)]
    return sorted(right_truncatable_primes, reverse=True)
