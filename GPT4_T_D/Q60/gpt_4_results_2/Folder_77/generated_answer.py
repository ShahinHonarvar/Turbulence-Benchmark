
import math

def all_left_right_truncatable_prime(numbers):
    x = numbers[767]
    
    def is_prime(n):
        if n == 0 or n == 1:
            return False
        if n == 2:
            return True
        if n % 2 == 0:
            return False
        sqrt_n = math.isqrt(n)
        for i in range(3, sqrt_n + 1, 2):
            if n % i == 0:
                return False
        return True

    def is_left_right_truncatable(n):
        if '0' in str(n):
            return False
        length = len(str(n))
        for i in range(length):
            left = int(str(n)[i:])
            right = int(str(n)[:length-i])
            if not is_prime(left) or not is_prime(right):
                return False
        return True

    result = [i for i in range(2, x + 1) if is_left_right_truncatable(i)]
    result.sort(reverse=True)

    return result
