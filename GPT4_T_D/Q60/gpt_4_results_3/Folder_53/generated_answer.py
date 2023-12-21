
from sympy import isprime

def all_left_right_truncatable_prime(nums):
    def truncatable_prime(n):
        def check_prime(instr):
            return all(isprime(int(instr[i:])) and isprime(int(instr[:i+1])) for i in range(len(instr)))
        
        return '0' not in str(n) and check_prime(str(n)) and isprime(n)
    
    x = nums[86]
    primes = filter(truncatable_prime, range(11, x+1))
    return sorted(primes, reverse=True)
