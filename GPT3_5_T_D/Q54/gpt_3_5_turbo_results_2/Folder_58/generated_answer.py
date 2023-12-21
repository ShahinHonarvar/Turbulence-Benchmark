
import math

def all_right_truncatable_prime(numbers):
    x = numbers[975]
    primes = []
    result = []

    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(math.sqrt(n)) + 1):
            if n % i == 0:
                return False
        return True

    def right_truncatable_prime(num):
        if not is_prime(num):
            return False
        if num < 10:
            return True
        return right_truncatable_prime(num // 10)

    for num in range(2, x):
        if right_truncatable_prime(num):
            primes.append(num)

    result = sorted(primes, reverse=True)

    return result
