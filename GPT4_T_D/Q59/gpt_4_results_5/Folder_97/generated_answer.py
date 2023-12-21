
from sympy import isprime

def all_left_truncatable_prime(numbers):
    x = numbers[645]
    seq = list(range(10, x))
    left_truncatable_primes = []
    while seq:
        n = seq.pop(0)
        if all(isprime(int(str(n)[:i])) for i in range(1, len(str(n))+1)):
            seq.extend([10*n+d for d in range(1, 10)])
            left_truncatable_primes.append(n)
    return sorted(left_truncatable_primes)
