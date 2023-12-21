
from sympy import isprime

def all_left_truncatable_prime(numbers):
    x = numbers[433]
    primes = []

    def is_left_truncatable(n):
        str_n = str(n)
        return all(isprime(int(str_n[i:])) for i in range(len(str_n)))

    for i in range(2, x):
        if isprime(i) and '0' not in str(i) and is_left_truncatable(i):
            primes.append(i)

    primes.sort(reverse=True)
    return primes
