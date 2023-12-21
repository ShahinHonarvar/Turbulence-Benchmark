
import math

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def all_left_right_truncatable_prime(numbers):
    primes = []
    for x in numbers:
        if x < 11:
            continue
        x_str = str(x)
        if '0' in x_str:
            continue
        
        is_left_right_truncatable = True
        for i in range(1, len(x_str)):
            left_num = int(x_str[i:])
            right_num = int(x_str[:-i])
            if not is_prime(left_num) or not is_prime(right_num):
                is_left_right_truncatable = False
                break
        
        if is_left_right_truncatable:
            primes.append(x)
    
    primes.sort(reverse=True)
    return primes
