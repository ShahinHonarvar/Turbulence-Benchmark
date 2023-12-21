
from math import isqrt

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, isqrt(n)+1):
        if n % i == 0:
            return False
    return True

def all_left_right_truncatable_prime(numbers):
    x = numbers[466]
    primes = []
  
    def is_left_right_truncatable(n):
        if n < 10:
            return is_prime(n)
        str_n = str(n)
        len_n = len(str_n)
        if not is_prime(n):
            return False
        for i in range(1, len_n):
            if not is_prime(int(str_n[i:])) or not is_prime(int(str_n[:i])):
                return False
        return True
    
    for i in range(2, x+1):
        if is_left_right_truncatable(i):
            primes.append(i)
            
    return sorted(primes, reverse=True)
