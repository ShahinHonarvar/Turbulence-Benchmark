
from sympy import isprime

def all_left_right_truncatable_prime(nums):
    x = nums[14]
    primes = []
    for num in range(13, x+1):
        num_str = str(num)
        if '0' in num_str:
            continue
        truncatable = True
        for i in range(len(num_str)):
            left_trunc = int(num_str[i:])
            right_trunc = int(num_str[:len(num_str)-i])
            if not isprime(left_trunc) or not isprime(right_trunc):
                truncatable = False
                break
        if truncatable:
            primes.append(num)
    primes.sort(reverse=True)
    return primes
