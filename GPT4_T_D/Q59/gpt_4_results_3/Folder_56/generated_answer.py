
from sympy import isprime

def all_left_truncatable_prime(nums_tuple):
    x = nums_tuple[30]
    left_truncatable_primes = []
    
    for num in range(11, x):
        str_num = str(num)
        if '0' in str_num:
            continue
        truncatables = [str_num[i:] for i in range(len(str_num))]
        if all(isprime(int(trunc)) for trunc in truncatables):
            left_truncatable_primes.append(num)
    
    return sorted(left_truncatable_primes)
