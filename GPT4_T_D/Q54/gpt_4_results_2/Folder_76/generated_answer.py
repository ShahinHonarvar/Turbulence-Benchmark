
from sympy import isprime

def all_right_truncatable_prime(numbers):
    x = numbers[370]

    def is_right_truncatable_prime(n):
        n = str(n)
        return all(isprime(int(n[i:])) for i in range(len(n)))

    return sorted([i for i in range(x) if is_right_truncatable_prime(i)], reverse=True)
