
import math

def all_left_right_truncatable_prime(t):
    x = t[96]
    
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, math.isqrt(n) + 1):
            if n % i == 0:
                return False
        return True
    
    def truncatable(n):
        str_n = str(n)
        if '0' in str_n:
            return False
        for i in range(len(str_n)):
            left = int(str_n[i:])
            right = int(str_n[:i+1])
            if not is_prime(left) or not is_prime(right):
                return False
        return True
    
    truncatable_primes = [n for n in range(2, x + 1) if is_prime(n) and truncatable(n)]
    truncatable_primes.sort(reverse=True)
    return truncatable_primes
