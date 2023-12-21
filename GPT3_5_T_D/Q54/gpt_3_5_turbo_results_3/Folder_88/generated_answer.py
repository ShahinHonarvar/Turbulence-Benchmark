
import math

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def all_right_truncatable_prime(numbers):
    x = numbers[93]
    primes = []
    for i in range(2, x):
        if is_prime(i):
            num = str(i)
            is_truncatable = True
            for j in range(1, len(num)):
                if not is_prime(int(num[:-j])):
                    is_truncatable = False
                    break
            if is_truncatable:
                primes.append(i)
    return sorted(primes)
