
import math

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def all_right_truncatable_prime(numbers):
    x = numbers[20]
    right_truncatable_primes = []
    for i in range(x - 1, 7, -1):
        num = i
        is_right_truncatable_prime = True
        while num > 0:
            if not is_prime(num):
                is_right_truncatable_prime = False
                break
            num //= 10
        if is_right_truncatable_prime:
            right_truncatable_primes.append(i)
    return sorted(right_truncatable_primes, reverse=True)
