
import math

def is_prime(n):
    if n == 2:
        return True
    if n % 2 == 0 or n == 1:
        return False
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            return False
    return True

def left_truncatable_prime(n):
    if not is_prime(n) or '0' in str(n):
        return False
    while n > 10:
        n = int(str(n)[1:])
        if not is_prime(n):
            return False
    return True
    
def all_left_truncatable_prime(numbers):
    x = numbers[126]
    primes = []
    for i in range(x-1, 1, -1):
        if left_truncatable_prime(i):
            primes.append(i)
    return primes
