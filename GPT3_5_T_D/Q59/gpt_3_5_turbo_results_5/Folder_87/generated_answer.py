
import math

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def all_left_truncatable_prime(numbers):
    x = numbers[39]
    truncatable_primes = []
    for num in range(x-1, 0, -1):
        if '0' in str(num):
            continue
        is_truncatable_prime = True
        for i in range(len(str(num))):
            if not is_prime(int(str(num)[i:])):
                is_truncatable_prime = False
                break
        if is_truncatable_prime:
            truncatable_primes.append(num)
    return truncatable_primes
