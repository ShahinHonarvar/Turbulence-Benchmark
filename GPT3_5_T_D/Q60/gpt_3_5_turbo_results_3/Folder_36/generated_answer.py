
import math

def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            return False
    return True

def all_left_right_truncatable_prime(numbers):
    primes = []
    for x in numbers:
        if not is_prime(x):
            continue

        digits = list(str(x))
        while len(digits) > 1:
            if not is_prime(int(''.join(digits))):
                break
            digits.pop(0)
            if not is_prime(int(''.join(digits))):
                break
            digits.pop(-1)
        else:
            primes.append(x)

    primes.sort()
    return primes
