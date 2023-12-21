
import math

def all_left_truncatable_prime(numbers):
    def is_prime(n):
        if n == 2:
            return True
        if n < 2 or n % 2 == 0:
            return False
        sqrt_n = int(math.sqrt(n))
        for i in range(3, sqrt_n + 1, 2):
            if n % i == 0:
                return False
        return True

    x = numbers[77]
    result = []
    for i in range(x-1, 0, -1):
        if '0' in str(i):
            continue
        is_truncatable_prime = True
        trunc_i = i
        while trunc_i > 0:
            if not is_prime(trunc_i):
                is_truncatable_prime = False
                break
            trunc_i //= 10
        if is_truncatable_prime:
            result.append(i)
    return sorted(result, reverse=True)
