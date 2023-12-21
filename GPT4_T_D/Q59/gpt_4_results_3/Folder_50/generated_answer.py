
import math

def is_prime(n):
    if n == 1: 
        return False
    for i in range(2,int(math.sqrt(n))+1):
        if n % i == 0:
            return False
    return True

def is_left_truncatable_prime(n):
    if '0' in str(n):
        return False
    for i in range(1, len(str(n))):
        if not is_prime(int(str(n)[i:])):
            return False
    return True

def all_left_truncatable_prime(t):
    x = t[57]
    primes = [i for i in range(2, x) if is_prime(i) and is_left_truncatable_prime(i)]
    primes.sort(reverse=True)
    return primes
