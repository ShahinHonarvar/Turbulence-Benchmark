
import math

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def is_truncatable_prime(n):
    num_str = str(n)
    while len(num_str) > 1:
        if not is_prime(int(num_str)):
            return False
        num_str = num_str[1:-1]
    return is_prime(int(num_str))

def all_left_right_truncatable_prime(t):
    x = t[70]
    primes = []
    for i in range(2, x+1):
        if is_prime(i) and is_truncatable_prime(i):
            primes.append(i)
    return primes
