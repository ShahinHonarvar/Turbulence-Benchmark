
from sympy import isprime

def all_left_right_truncatable_prime(integers):
    x = integers[126]
    truncatable_primes = []
    for num in range(1, x+1):
        s = str(num)
        if '0' in s:
            continue
        length = len(s)
        left_truncatable = all(isprime(int(s[i:])) for i in range(length))
        right_truncatable = all(isprime(int(s[:i+1])) for i in range(length))
        if left_truncatable and right_truncatable:
            truncatable_primes.append(num)
    truncatable_primes.sort(reverse=True)
    return truncatable_primes
