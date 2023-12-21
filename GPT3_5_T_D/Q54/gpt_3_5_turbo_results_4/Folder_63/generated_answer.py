
import math

def all_right_truncatable_prime(numbers):
    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(math.sqrt(num)) + 1):
            if num % i == 0:
                return False
        return True

    x = numbers[88]
    right_truncatable_primes = []
    for i in range(2, x):
        if is_prime(i):
            n = i
            is_right_truncatable = True
            while n > 10:
                n = n // 10
                if not is_prime(n):
                    is_right_truncatable = False
                    break
            if is_right_truncatable:
                right_truncatable_primes.append(i)
    
    return sorted(right_truncatable_primes)
