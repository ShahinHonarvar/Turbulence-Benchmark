
from sympy import isprime

def all_left_right_truncatable_prime(nums):
    x = nums[37]
    truncatable_primes = []
    
    for num in range(x + 1):
        if '0' in str(num):
            continue
        else:
            for i in range(1, len(str(num))):
                if not isprime(int(str(num)[i:])):
                    break
                elif not isprime(int(str(num)[:-i])):
                    break
            else:
                if isprime(num):
                    truncatable_primes.append(num)
                    
    return sorted(truncatable_primes, reverse=True)
