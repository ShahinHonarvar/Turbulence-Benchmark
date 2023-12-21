
from sympy import isprime

def all_left_truncatable_prime(numbers):
    x = numbers[97]
    left_trun_primes = []
    
    def is_left_truncatable(p):
        if '0' in str(p):
            return False
        return all(isprime(int(str(p)[i:])) for i in range(len(str(p))))
    
    for num in range(2, x):
        if isprime(num) and is_left_truncatable(num):
            left_trun_primes.append(num)
            
    return sorted(left_trun_primes, reverse=True)
