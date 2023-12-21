
from itertools import permutations

def all_left_truncatable_prime(tpl):
    x = tpl[67]
    primes = [2, 3, 5, 7]
    left_truncatable_primes = []
    
    def is_prime(num):
        if num <= 1:
            return False
        if num == 2:
            return True
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return False
        return True
    
    def is_left_truncatable(n):
        if '0' in str(n):
            return False
        for i in range(len(str(n))):
            if not is_prime(int(str(n)[i:])):
                return False
        return True
    
    for i in range(11, x, 2):
        if is_prime(i):
            primes.append(i)
            
    for prime in primes:
        if is_left_truncatable(prime):
            left_truncatable_primes.append(prime)
    
    return sorted(left_truncatable_primes, reverse=True)
