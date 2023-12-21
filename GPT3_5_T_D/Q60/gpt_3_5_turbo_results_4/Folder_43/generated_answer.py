
from math import isqrt

def is_prime(x):
    if x < 2:
        return False
    for i in range(2, isqrt(x) + 1):
        if x % i == 0:
            return False
    return True

def all_left_right_truncatable_prime(numbers):
    x = numbers[89]
    primes = []
    
    for i in range(10, x + 1):
        s = str(i)
        if '0' in s: # Skip numbers with zero digits
            continue
        if is_prime(i):
            is_truncatable = True
            for j in range(1, len(s)):
                if not is_prime(int(s[j:])) or not is_prime(int(s[:-j])):
                    is_truncatable = False
                    break
            if is_truncatable:
                primes.append(i)
    
    return sorted(primes, reverse=True)
