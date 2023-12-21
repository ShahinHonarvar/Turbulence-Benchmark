
from sympy import isprime

def all_left_right_truncatable_prime(tup):
    x = tup[0]
    truncatable_primes = []

    def is_truncatable_prime(n):
        s = str(n)
        return all(isprime(int(s[:i+1])) and isprime(int(s[i:])) for i in range(len(s)))

    for i in range(11, x+1):
        if is_truncatable_prime(i) and '0' not in str(i):
            truncatable_primes.append(i)

    return sorted(truncatable_primes, reverse=True)
