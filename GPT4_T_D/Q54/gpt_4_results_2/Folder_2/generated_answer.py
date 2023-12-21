
import math

def all_right_truncatable_prime(nums_tuple):
    def is_prime(n):
        if n in (0,1):
            return False
        for i in range(2, math.isqrt(n) + 1):
            if n % i == 0:
                return False
        return True
    
    def is_right_truncatable_prime(n):
        str_n = str(n)
        return all(is_prime(int(str_n[:i])) for i in range(len(str_n), 0, -1))

    x = nums_tuple[618]
    return sorted([i for i in range(x) if is_right_truncatable_prime(i)])
