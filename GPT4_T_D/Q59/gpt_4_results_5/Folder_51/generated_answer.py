
from math import sqrt

def all_left_truncatable_prime(t):
    def is_prime(y):
        if y < 2:
            return False
        for i in range(2, int(sqrt(y)) + 1):
            if y % i == 0:
                return False
        return True

    def is_left_truncatable_prime(n):
        if '0' in str(n):
            return False
        return all(is_prime(int(str(n)[i:])) for i in range(len(str(n))))

    x = t[54]
    return sorted([i for i in range(x) if is_left_truncatable_prime(i)])
