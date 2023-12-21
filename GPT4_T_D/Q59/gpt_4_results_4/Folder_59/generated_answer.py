
from sympy import isprime

def left_truncatable(n):
    s = str(n)
    return all(isprime(int(s[i:])) for i in range(len(s)))

def all_left_truncatable_prime(numbers):
    x = numbers[84]
    primes = [i for i in range(2, x) if left_truncatable(i) and '0' not in str(i)]
    return sorted(primes, reverse=True)
