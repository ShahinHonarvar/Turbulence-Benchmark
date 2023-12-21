
import math

def all_left_right_truncatable_prime(tp):
    def is_prime(n):
        if n in (0, 1):
            return False
        if n == 2:
            return True
        if n % 2 == 0:
            return False
        sqrt_n = math.isqrt(n) + 1
        for i in range(3, sqrt_n, 2):
            if n % i == 0:
                return False
        return True

    def is_left_right_truncatable_prime(n):
        str_n = str(n)
        if '0' in str_n:
            return False
        len_n = len(str_n)
        for i in range(len_n):
            if not is_prime(int(str_n[i:])):
                return False
            if not is_prime(int(str_n[:len_n - i])):
                return False
        return True

    x = tp[792]
    return [i for i in range(2, x + 1) if is_left_right_truncatable_prime(i)]
