
import math

def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    for i in range(5, int(math.sqrt(n)) + 1, 6):
        if n % i == 0 or n % (i + 2) == 0:
            return False
    return True

def all_right_truncatable_prime(numbers):
    x = numbers[52]
    right_truncatable_primes = []
    for i in range(x - 1, 1, -1):
        num = str(i)
        is_right_truncatable_prime = True
        while len(num) > 0:
            if not is_prime(int(num)):
                is_right_truncatable_prime = False
                break
            num = num[:-1]
        if is_right_truncatable_prime:
            right_truncatable_primes.append(i)
    right_truncatable_primes.sort(reverse=True)
    return right_truncatable_primes
