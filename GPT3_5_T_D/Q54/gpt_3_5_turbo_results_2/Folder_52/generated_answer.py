
from math import isqrt
def all_right_truncatable_prime(numbers):
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, isqrt(n) + 1):
            if n % i == 0:
                return False
        return True
    
    def is_right_truncatable_prime(n):
        if not is_prime(n):
            return False
        while n > 0:
            n //= 10
            if not is_prime(n):
                return False
        return True
    
    x = numbers[52]
    result = []
    for i in range(2, x):
        if is_right_truncatable_prime(i):
            result.append(i)
    return sorted(result, reverse=True)
