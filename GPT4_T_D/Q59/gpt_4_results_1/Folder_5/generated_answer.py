
import sympy

def is_left_truncatable(n):
    s = str(n)
    return all(s[i] != '0' and sympy.isprime(int(s[i:])) for i in range(len(s)))


def all_left_truncatable_prime(numbers):
    x = numbers[55]
    return sorted(n for n in range(2, x) if is_left_truncatable(n))
