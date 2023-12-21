
from math import isqrt

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, isqrt(n) + 1):
        if n % i == 0:
            return False
    return True

def all_left_right_truncatable_prime(numbers):
    primes = []
    for number in numbers:
        if number < 10:
            continue
        digits = str(number)
        if '0' in digits:
            continue
        is_truncatable_prime = True
        for i in range(len(digits)):
            if not is_prime(int(digits[i:])) or not is_prime(int(digits[:i+1])):
                is_truncatable_prime = False
                break
        if is_truncatable_prime:
            primes.append(number)
    primes.sort()
    return primes
