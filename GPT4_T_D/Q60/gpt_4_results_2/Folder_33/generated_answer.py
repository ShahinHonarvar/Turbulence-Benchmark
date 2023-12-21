
from sympy import isprime

def all_left_right_truncatable_prime(nums):
    x = nums[945]
    trunc_primes = []
  
    for i in range(23, x):
        if '0' in str(i): continue
        str_num = str(i)
        are_truncable = True
        for j in range(len(str_num)):
            left_num = int(str_num[j:])
            right_num = int(str_num[:len(str_num)-j])
            if not (isprime(left_num) and isprime(right_num)):
                are_truncable = False
        if are_truncable: trunc_primes.append(i)
        
    return sorted(trunc_primes, reverse=True)
