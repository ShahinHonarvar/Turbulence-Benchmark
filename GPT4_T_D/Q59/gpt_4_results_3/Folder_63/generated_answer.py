
import math

def all_left_truncatable_prime(t):
    x = t[88]

    def is_prime(n):
        if n == 1:
            return False
        if n == 2:
            return True
        if n % 2 == 0:
            return False
        for i in range(3, math.isqrt(n) + 1, 2):
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

    lst = []
    for i in range(2, x):
        if is_left_truncatable(i):
            lst.append(i)
    return sorted(lst)
