
from sympy import isprime

def all_left_truncatable_prime(tup):
    x = tup[70]
    truncated_primes = []

    def is_left_truncatable(n):
        str_n = str(n)
        return all(isprime(int(str_n[i:])) for i in range(len(str_n)))

    for num in range(2, x):
        if "0" not in str(num) and isprime(num) and is_left_truncatable(num):
            truncated_primes.append(num)
    return sorted(truncated_primes, reverse=True)
