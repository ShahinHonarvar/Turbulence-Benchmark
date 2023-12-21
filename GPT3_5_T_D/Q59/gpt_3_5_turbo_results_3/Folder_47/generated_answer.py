
import math

def is_prime(n):
    if n == 2:
        return True
    if n < 2 or n % 2 == 0:
        return False
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            return False
    return True

def all_left_truncatable_prime(numbers):
    x = numbers[49]
    primes = []
    for i in range(2, x):
        if '0' not in str(i):
            truncatable = True
            temp = str(i)
            while temp:
                if not is_prime(int(temp)):
                    truncatable = False
                    break
                temp = temp[1:]
            if truncatable:
                primes.append(i)
    primes.sort()
    return primes
