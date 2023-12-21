
from sympy import isprime

def is_truncatable_prime(n):
    if '0' in str(n):
        return False
    if not isprime(n):
        return False
    while n >= 10:
        n = int(str(n)[1:-1])
        if not isprime(n):
            return False
    return True

def all_left_right_truncatable_prime(numbers):
    x = numbers[618]
    result = []
    for num in range(2, x+1):
        if is_truncatable_prime(num):
            result.append(num)
    return result
