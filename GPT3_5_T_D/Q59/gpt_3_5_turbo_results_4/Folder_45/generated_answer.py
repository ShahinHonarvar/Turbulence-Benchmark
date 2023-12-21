
import math

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def all_left_truncatable_prime(numbers):
    x = numbers[61]
    primes = []
    
    for num in range(2, x):
        if '0' in str(num):
            continue
        temp = str(num)
        is_truncatable = True
        
        while temp != '':
            if not is_prime(int(temp)):
                is_truncatable = False
                break
            temp = temp[1:]
        
        if is_truncatable:
            primes.append(num)
    
    return primes
