
import math

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def all_left_truncatable_prime(numbers):
    x = numbers[65]
    primes = []
    
    for num in range(2, x):
        if not '0' in str(num):
            prime = True
            for i in range(1, len(str(num))):
                if not is_prime(int(str(num)[i:])):
                    prime = False
                    break
            if prime:
                primes.append(num)
    
    return sorted(primes, reverse=True)
