
from sympy import isprime

def all_right_truncatable_prime(numbers):
    def is_right_truncatable_prime(n):
        s = str(n)
        return all(isprime(int(s[:i])) for i in range(1, len(s)+1))

    x = numbers[81]
    return sorted([i for i in range(2, x) if is_right_truncatable_prime(i)], reverse=True)
