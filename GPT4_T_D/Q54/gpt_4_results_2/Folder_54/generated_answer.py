
import math

def all_right_truncatable_prime(tup):
    x = tup[88]
    
    def is_prime(n):
        if n < 2: return False
        for i in range(2, int(math.sqrt(n))+1):
            if n % i == 0:
                return False
        return True

    def is_right_truncatable_prime(n):
        if not is_prime(n): return False
        while n > 0:
            n //= 10
            if n != 0 and not is_prime(n):
                return False
        return True

    output = [n for n in range(2, x) if is_right_truncatable_prime(n)]
    return sorted(output, reverse=True)
