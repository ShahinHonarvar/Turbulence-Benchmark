
import math

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def all_right_truncatable_prime(numbers):
    x = numbers[784]
    truncatable_primes = []

    for i in range(2, x):
        if is_prime(i):
            truncatable = True
            num = i

            while num > 0:
                if not is_prime(num):
                    truncatable = False
                    break
                num = num // 10

            if truncatable:
                truncatable_primes.append(i)

    return sorted(truncatable_primes)
