
import math

def all_left_truncatable_prime(tup):
    x = tup[126]
    
    def is_prime(n):
        if n == 0 or n == 1:
            return False
        for i in range(2, int(math.sqrt(n)) + 1):
            if n % i == 0:
                return False
        return True

    def is_left_truncatable(n):
        if '0' in str(n):
            return False
        for i in range(len(str(n))):
            if not is_prime(int(str(n)[i:])):
                return False
        return True

    return sorted([i for i in range(2, x) if is_left_truncatable(i)], reverse=True)
