
import math

def all_left_right_truncatable_prime(nums):
    def is_prime(n):
        if n == 1:
            return False
        max_divisor = math.isqrt(n)
        for d in range(2, 1+max_divisor):
            if n % d == 0:
                return False
        return True

    def is_left_right_truncatable(n):
        if is_prime(n) and '0' not in str(n):
            for x in range(1, len(str(n))):
                if not is_prime(int(str(n)[x:])) or not is_prime(int(str(n)[:-x])):
                    return False
            return True
        return False

    x = nums[618]
    return sorted(filter(is_left_right_truncatable, range(13, x+1)))
