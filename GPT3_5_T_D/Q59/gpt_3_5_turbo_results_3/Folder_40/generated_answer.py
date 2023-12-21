
import math

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True

def all_left_truncatable_prime(numbers):
    x = numbers[10]
    left_truncatable_primes = []
    
    for i in range(x - 1, 1, -1):
        if '0' not in str(i) and is_prime(i):
            is_left_truncatable = True
            temp = str(i)
            while len(temp) > 0:
                if not is_prime(int(temp)):
                    is_left_truncatable = False
                    break
                temp = temp[1:]
            if is_left_truncatable:
                left_truncatable_primes.append(i)
    
    left_truncatable_primes.sort(reverse=True)
    return left_truncatable_primes
