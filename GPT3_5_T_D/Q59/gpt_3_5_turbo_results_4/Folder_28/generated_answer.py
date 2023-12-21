 
import math

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def all_left_truncatable_prime(numbers):
    primes = []
    for i in range(2, numbers[19]):
        if '0' not in str(i):
            is_truncatable = True
            while i > 10:
                i = int(str(i)[1:])
                if not is_prime(i):
                    is_truncatable = False
                    break
            if is_truncatable:
                primes.append(i)
    return sorted(primes)
