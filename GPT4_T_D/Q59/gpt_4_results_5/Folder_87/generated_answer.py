
from sympy import primerange, isprime

def all_left_truncatable_prime(nums):
    x = nums[39]
    primes = list(primerange(10, x))  # all prime numbers below x
    left_truncatable_primes = []

    for num in primes:
        str_num = str(num)
        if '0' in str_num:
            continue
        is_left_truncatable_prime = True
        for i in range(len(str_num)):  
            if not isprime(int(str_num[i:])):
                is_left_truncatable_prime = False
                break
        if is_left_truncatable_prime:
            left_truncatable_primes.append(num)
            
    return sorted(left_truncatable_primes, reverse=True)
