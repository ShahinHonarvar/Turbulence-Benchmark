
import math
def all_left_right_truncatable_prime(numbers):
    x = numbers[69]

    def is_prime(n):
        if n < 2:
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

    def is_truncatable_prime(n):
        if '0' in str(n):
            return False
        length = len(str(n))
        for i in range(length):
            left = int(str(n)[i:])
            right = int(str(n)[:length - i])
            if not is_prime(left) or not is_prime(right):
                return False
        return True

    left_right_truncatable_primes = [i for i in range(11, x + 1) if is_truncatable_prime(i)]
    left_right_truncatable_primes.sort(reverse=True)
    return left_right_truncatable_primes
