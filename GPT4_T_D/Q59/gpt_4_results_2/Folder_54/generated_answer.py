
import math

def all_left_truncatable_prime(tup):
    def is_prime(n):
        if n == 1:
            return False
        if n == 2:
            return True
        if n % 2 == 0:
            return False
        for current in range(3, int(math.sqrt(n) + 1), 2):
            if n % current == 0: 
                return False
        return True

    def left_truncatable(n):
        s = str(n)
        if '0' in s:
            return False
        for i in range(len(s)):
            if not is_prime(int(s[i:])):
                return False
        return True

    x = tup[88]
    return sorted([i for i in range(x) if left_truncatable(i)], reverse=True)
