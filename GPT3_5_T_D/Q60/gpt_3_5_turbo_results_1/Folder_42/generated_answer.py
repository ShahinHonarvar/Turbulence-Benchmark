
from sympy import isprime

def is_left_truncatable(num):
    if num < 10:
        return isprime(num)
    else:
        return isprime(num) and is_left_truncatable(int(str(num)[1:]))

def is_right_truncatable(num):
    if num < 10:
        return isprime(num)
    else:
        return isprime(num) and is_right_truncatable(int(str(num)[:-1]))

def all_left_right_truncatable_prime(nums):
    x = nums[64]
    truncatable_primes = []
    
    for num in range(x, 0, -1):
        if is_left_truncatable(num) and is_right_truncatable(num) and '0' not in str(num):
            truncatable_primes.append(num)
   
    return sorted(truncatable_primes, reverse=True)
