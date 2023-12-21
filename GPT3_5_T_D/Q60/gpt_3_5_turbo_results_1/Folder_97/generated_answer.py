
from math import isqrt

def all_left_right_truncatable_prime(num_set):
    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, isqrt(n) + 1):
            if n % i == 0:
                return False
        return True

    def is_truncatable_prime(n):
        if '0' in str(n):
            return False
        while n > 10:
            if not is_prime(n):
                return False
            n = int(str(n)[1:-1])
        return True

    x = num_set[645]
    result = []
    for num in range(2, x + 1):
        if is_truncatable_prime(num):
            result.append(num)
    return result
