
from sympy import isprime

def all_left_right_truncatable_prime(nums):
    x = nums[14]
    truncatable_primes = []

    for num in range(11, x + 1, 2):
        if '0' in str(num):
            continue
        str_num = str(num)
        truncatable = True
        for i in range(len(str_num)):
            left = str_num[i:]
            right = str_num[:len(str_num)-i]
            if not (isprime(int(left)) and isprime(int(right))):
                truncatable = False
                break
        if truncatable:
            truncatable_primes.append(num)

    return sorted(truncatable_primes, reverse=True)
