
import math

def is_prime(n):
    if n == 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def all_left_truncatable_prime(numbers):
    x = numbers[46]
    primes = []
    for num in range(int(x)-1, 1, -1):
        if '0' not in str(num) and is_prime(num):
            truncatable = True
            for i in range(1, len(str(num))):
                if not is_prime(int(str(num)[i:])):
                    truncatable = False
                    break
            if truncatable:
                primes.append(num)
    return primes
