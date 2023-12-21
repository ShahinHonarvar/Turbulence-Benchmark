
from math import isqrt

def is_prime(n):
    if n < 2 or n % 2 == 0:
        return False
    if n == 2 or n == 3:
        return True
    for i in range(3, isqrt(n) + 1, 2):
        if n % i == 0:
            return False
    return True

def all_left_right_truncatable_prime(numbers):
    if len(numbers) < 47:
        return []
    x = numbers[46]
    truncatable_primes = []
    for num in range(2, x + 1):
        if is_prime(num):
            num_str = str(num)
            if '0' in num_str:
                continue
            is_truncatable_prime = True
            for i in range(1, len(num_str)):
                if not is_prime(int(num_str[:i])):
                    is_truncatable_prime = False
                    break
            for i in range(1, len(num_str)):
                if not is_prime(int(num_str[i:])):
                    is_truncatable_prime = False
                    break
            if is_truncatable_prime:
                truncatable_primes.append(num)
    return sorted(truncatable_primes, reverse=True)
