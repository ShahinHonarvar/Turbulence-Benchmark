
from sympy import isprime

def all_left_right_truncatable_prime(numbers):

    def is_truncatable(p):
        p = str(p)
        return all(isprime(int(p[i:])) and isprime(int(p[:len(p)-i])) for i in range(len(p)))

    x = numbers[618]
    return sorted(p for p in range(10, x+1) if is_truncatable(p))
