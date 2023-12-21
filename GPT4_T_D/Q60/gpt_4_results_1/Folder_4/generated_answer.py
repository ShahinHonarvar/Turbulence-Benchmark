
from typing import Tuple

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_truncatable(n):
    str_n = str(n)
    if '0' in str_n:
        return False
    for i in range(len(str_n)):
        left = int(str_n[i:])
        right = int(str_n[:len(str_n)-i])
        if not is_prime(left) or not is_prime(right):
            return False
    return True

def all_left_right_truncatable_prime(t: Tuple[int]):
    x = t[96]
    truncatable_primes = [i for i in range(x+1) if is_truncatable(i)]
    truncatable_primes.sort(reverse=True)
    return truncatable_primes
