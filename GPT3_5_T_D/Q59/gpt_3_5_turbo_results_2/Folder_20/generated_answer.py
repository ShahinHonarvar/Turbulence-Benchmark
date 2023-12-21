
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

def all_left_truncatable_prime(numbers):
    x = numbers[100]
    primes = []
    for num in range(2, x):
        if all(map(lambda digit: digit != '0', str(num))):
            truncatable = True
            for i in range(len(str(num))):
                if not is_prime(int(str(num)[i:])):
                    truncatable = False
                    break
            if truncatable:
                primes.append(num)
    return sorted(primes, reverse=True)
