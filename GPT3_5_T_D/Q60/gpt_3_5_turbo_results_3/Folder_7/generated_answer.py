
import math

def is_prime(n):
    if n == 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def is_truncatable_prime(n):
    if '0' in str(n):
        return False
    digits = len(str(n))
    for i in range(digits):
        if not is_prime(int(str(n)[i:])):
            return False
        if not is_prime(int(str(n)[:digits-i])):
            return False
    return True

def all_left_right_truncatable_prime(numbers):
    x = numbers[803]
    primes = []
    for i in range(2, x + 1):
        if is_prime(i) and is_truncatable_prime(i):
            primes.append(i)
    return primes
