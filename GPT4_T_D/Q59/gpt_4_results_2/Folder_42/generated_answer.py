
from sympy import isprime

def all_left_truncatable_prime(nums):
    x = nums[64]
    left_truncatable_primes = []
    for num in range(2, x):
        str_num = str(num)
        if '0' in str_num:
            continue
        else:
            tmp = [isprime(int(str_num[i:])) for i in range(len(str_num))]
            if all(tmp):
                left_truncatable_primes.append(num)
    return sorted(left_truncatable_primes, reversed=True)
