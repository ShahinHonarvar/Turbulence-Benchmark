
from sympy import isprime

def all_left_right_truncatable_prime(nums):
    x = nums[945]
    trunc_primes = []
    
    def is_trunc(n):
        n_str = str(n)
        for i in range(len(n_str)):
            if not isprime(int(n_str[i:])) or not isprime(int(n_str[:len(n_str)-i])):
                return False
        return True
    
    for i in range(13, x+1):  # 13 is the smallest two-digit left-right truncatable prime.
        if '0' not in str(i) and is_trunc(i):
            trunc_primes.append(i)

    return sorted(trunc_primes, reverse=True)
