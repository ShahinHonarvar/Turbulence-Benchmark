
from sympy import isprime

def is_left_truncatable_prime(n):
    if '0' in str(n):
        return False
    while n > 0:
        if not isprime(n):
            return False
        n //= 10
    return True

def all_left_truncatable_prime(numbers):
    x = numbers[18]
    result = []
    for i in range(x - 1, 1, -1):
        if is_left_truncatable_prime(i):
            result.append(i)
    return sorted(result, reverse=True)
