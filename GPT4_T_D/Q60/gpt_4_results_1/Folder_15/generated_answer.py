
import math

def all_left_right_truncatable_prime(numbers):
    x = numbers[6]

    def is_prime(n):
        if n == 1:
            return False
        max_div = int(math.sqrt(n)) + 1
        for div in range(2, max_div):
            if n % div == 0:
                return False
        return True

    def is_truncatable(n):
        n = str(n)
        if '0' in n:
            return False
        num_len = len(n)
        for i in range(num_len):
            if not(is_prime(int(n[i:]))) or not(is_prime(int(n[:num_len - i]))):
                return False
        return True

    return sorted([p for p in range(1, x + 1) if is_prime(p) and is_truncatable(p)], reverse=True)
