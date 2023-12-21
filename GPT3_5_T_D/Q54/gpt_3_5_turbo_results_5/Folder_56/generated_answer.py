
import math

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def all_right_truncatable_prime(numbers):
    x = numbers[30]
    right_truncatable_primes = []
    
    def is_right_truncatable_prime(n):
        if not is_prime(n):
            return False
        if n < 10:
            return True
        else:
            return is_right_truncatable_prime(n // 10)
    
    for num in range(2, x):
        if is_right_truncatable_prime(num):
            right_truncatable_primes.append(num)
    
    return sorted(right_truncatable_primes)
