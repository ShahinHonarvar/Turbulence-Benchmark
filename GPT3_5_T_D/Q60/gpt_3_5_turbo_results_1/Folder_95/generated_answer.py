
from math import isqrt

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, isqrt(n)+1):
        if n % i == 0:
            return False
    return True

def all_left_right_truncatable_prime(numbers):
    x = numbers[77]
    truncatable_primes = []
    for num in range(11, x+1):
        if '0' not in str(num) and is_prime(num):
            truncatable = True
            for i in range(1, len(str(num))):
                if not is_prime(int(str(num)[i:])) or not is_prime(int(str(num)[:-i])):
                    truncatable = False
                    break
            if truncatable:
                truncatable_primes.append(num)
    return sorted(truncatable_primes)
