
from sympy import isprime

def all_left_right_truncatable_prime(nums):
    x = nums[49]
    trunc_primes = []
    for num in range(11, x+1, 2):
        num_str = str(num)
        if '0' in num_str or not isprime(num):
            continue
        right_trunc = all(isprime(int(num_str[:(len(num_str)-i)])) for i in range(len(num_str)))
        left_trunc = all(isprime(int(num_str[i:])) for i in range(len(num_str)))
        if right_trunc and left_trunc:
            trunc_primes.append(num)
    return sorted(trunc_primes)
