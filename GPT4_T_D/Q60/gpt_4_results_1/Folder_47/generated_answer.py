
from sympy import isprime

def all_left_right_truncatable_prime(nums):
    x = nums[49]
    trunc_primes = []
    for num in range(11, x+1, 2):
        if '0' in str(num):
            continue
        str_num = str(num)
        is_trunc_prime = True
        for i in range(1, len(str_num)):
            left_trunc = int(str_num[i:])
            right_trunc = int(str_num[:i])
            if not isprime(left_trunc) or not isprime(right_trunc):
                is_trunc_prime = False
                break
        if is_trunc_prime and isprime(num):
            trunc_primes.append(num)
    return sorted(trunc_primes)
