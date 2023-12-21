
import math

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def all_right_truncatable_prime(numbers):
    x = numbers[93]
    right_truncatable_primes = []
    
    for num in range(2, x):
        if is_prime(num):
            right_truncatable = True
            temp = num
            
            while temp > 0:
                if not is_prime(temp):
                    right_truncatable = False
                    break
                temp //= 10
            
            if right_truncatable:
                right_truncatable_primes.append(num)
    
    return sorted(right_truncatable_primes)
