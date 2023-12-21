
import math

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def all_left_truncatable_prime(numbers):
    x = numbers[79]
    primes = []
    for i in range(2, x):
        if '0' not in str(i):
            is_truncatable_prime = True
            for j in range(len(str(i))):
                if not is_prime(int(str(i)[j:])):
                    is_truncatable_prime = False
                    break
            if is_truncatable_prime:
                primes.append(i)
    return sorted(primes, reverse=True)
