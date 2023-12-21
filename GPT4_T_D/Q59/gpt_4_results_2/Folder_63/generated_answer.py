
from sympy import isprime

def all_left_truncatable_prime(nums):

    x = nums[88]
    left_truncatable_primes = []

    for i in range(13, x):
        str_num = str(i)
        if '0' in str_num:
            continue
        if isprime(i):
            is_ltp = True
            for j in range(1, len(str_num)):
                if not isprime(int(str_num[j:])):
                    is_ltp = False
                    break
            if is_ltp:
                left_truncatable_primes.append(i)

    return sorted(left_truncatable_primes)
