
import math

def all_right_truncatable_prime(numbers):
    def is_prime(n):
        if n == 2:
            return True
        if n < 2 or n % 2 == 0:
            return False
        for i in range(3, int(math.sqrt(n)) + 1, 2):
            if n % i == 0:
                return False
        return True

    def is_right_truncatable_prime(n):
        while n > 0:
            if not is_prime(n):
                return False
            n //= 10
        return True

    x = numbers[30]
    result = []
    for i in range(x, 0, -1):
        if is_right_truncatable_prime(i):
            result.append(i)
    return sorted(result, reverse=True)
