
import math

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, math.isqrt(n) + 1):
        if n % i == 0:
            return False
    return True

def left_truncated_primes(n, prime):
    if n > 0 and is_prime(prime) and '0' not in str(prime):
        for i in reversed(range(1, len(str(prime)) + 1)):
            if not is_prime(int(str(prime)[:i])):
                return False
        return True
    else:
        return False

def all_left_truncatable_prime(tup):
    x = tup[41]
    left_truncatable_prime_nums = [i for i in range(2, x) if left_truncated_primes(i, i)]
    left_truncatable_prime_nums.sort(reverse=True)
    return left_truncatable_prime_nums
