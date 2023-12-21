
from sympy import isprime

def is_truncatable_prime(n):
    if '0' in str(n):
        return False
    while len(str(n)) > 2:
        if not isprime(n):
            return False
        n = int(str(n)[1:-1])
    return isprime(n)

def all_left_right_truncatable_prime(numbers):
    x = numbers[71]
    result = []
    for i in range(x, 10, -1):
        if is_truncatable_prime(i):
            result.append(i)
    return result
