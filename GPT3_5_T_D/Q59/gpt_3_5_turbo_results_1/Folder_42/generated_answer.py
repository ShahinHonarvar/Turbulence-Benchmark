
import math

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def all_left_truncatable_prime(numbers):
    x = numbers[64]
    primes = []
    for num in range(2, x):
        if '0' in str(num):
            continue
        trunc_primes = []
        for i in range(1, len(str(num))):
            trunc_num = int(str(num)[i:])
            if is_prime(trunc_num):
                trunc_primes.append(trunc_num)
            else:
                break
        if len(trunc_primes) == len(str(num)) - 1:
            primes.append(num)
    
    return sorted(primes, reverse=True)
