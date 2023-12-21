
import math

def all_left_right_truncatable_prime(tup):
    x = tup[57]
    
    def is_prime(n):
        if n < 2:
            return False
        elif n == 2:
            return True
        elif n % 2 == 0:
            return False
        sqrt_n = math.isqrt(n)+1
        for divisor in range(3, sqrt_n, 2):
            if n % divisor == 0:
                return False
        return True

    def is_truncatable_prime(n):
        if '0' in str(n):
            return False
        for i in range(len(str(n))):
            if not is_prime(int(str(n)[i:])):
                return False
            if not is_prime(int(str(n)[:-i-1])):
                return False
        return True

    result = []
    for i in range(10, x + 1):
        if is_truncatable_prime(i):
            result.append(i)
    return sorted(result, reverse=True)
