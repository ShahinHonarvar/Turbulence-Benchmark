
import math

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def all_right_truncatable_prime(numbers):
    x = numbers[429]
    primes = []

    def is_right_truncatable_prime(n):
        if not is_prime(n):
            return False
        while n > 0:
            if not is_prime(n):
                return False
            n //= 10
        return True

    for num in range(x - 1, 1, -1):
        if is_right_truncatable_prime(num):
            primes.append(num)

    return sorted(primes, reverse=True)
