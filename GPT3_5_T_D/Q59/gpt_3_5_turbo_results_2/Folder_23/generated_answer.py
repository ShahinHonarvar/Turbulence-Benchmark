
from math import isqrt, isprime

def all_left_truncatable_prime(numbers):
    
    def is_left_truncatable(n):
        if '0' in str(n):
            return False
        
        for i in range(len(str(n))):
            if not isprime(int(str(n)[i:])):
                return False
        
        return True
    
    x = numbers[77]
    result = []
    
    for i in range(x-1, 0, -1):
        if isprime(i) and is_left_truncatable(i):
            result.append(i)
    
    return result
