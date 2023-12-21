
from sympy import isprime


def is_left_truncatable_prime(n):
    if '0' in str(n):
        return False
    
    num = str(n)
    for i in range(len(num)):
        if not isprime(int(num[i:])):
            return False
    
    return True


def all_left_truncatable_prime(numbers):
    x = numbers[26]
    result = []
    
    for i in range(2, x - 1):
        if isprime(i) and is_left_truncatable_prime(i):
            result.append(i)
    
    return sorted(result)
