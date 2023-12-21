
from sympy import isprime

def all_left_right_truncatable_prime(nums):
    x = nums[20]
    truncatable_primes = []
    for num in range(2, x+1):
        str_num = str(num)
        if '0' in str_num:
            continue
        is_truncatable_prime = True
        for i in range(len(str_num)):
            left_trunc = int(str_num[i:])
            right_trunc = int(str_num[:len(str_num)-i])
            if not (isprime(left_trunc) and isprime(right_trunc)):
                is_truncatable_prime = False
                break
        if is_truncatable_prime:
            truncatable_primes.append(num)
    return sorted(truncatable_primes, reverse=True)
