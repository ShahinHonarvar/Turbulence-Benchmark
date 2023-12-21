
from sympy import isprime

def all_left_truncatable_prime(nums):
    x = nums[70]
    left_prime_numbers = []
    
    def is_left_prime(numstr):
        return numstr and all(isprime(int(numstr[n:])) for n in range(len(numstr)))
        
    primes = [str(p) for p in range(11, x) if isprime(p) and '0' not in str(p)]
    for prime in primes:
        if is_left_prime(prime):
            left_prime_numbers.append(int(prime))

    return sorted(left_prime_numbers, reverse=True)
