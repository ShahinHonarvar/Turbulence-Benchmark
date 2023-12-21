
import math

def all_right_truncatable_prime(numbers):
    def is_prime(num):
        if num == 1:
            return False
        if num == 2:
            return True
        if num % 2 == 0:
            return False
        for i in range(3, math.isqrt(num) + 1, 2):
            if num % i == 0:
                return False
        return True

    def is_right_truncatable_prime(num):
        while num != 0:
            if not is_prime(num):
                return False
            num //= 10
        return True

    x = numbers[91]
    prime_list = []
    for i in range(2, x):
        if is_right_truncatable_prime(i):
            prime_list.append(i)

    return sorted(prime_list)
