
from sympy import isprime

def all_left_truncatable_prime(nums):
    x = nums[87]
    primes = []
    for num in range(2, x):
        str_num = str(num)
        if '0' in str_num:
            continue
        is_trunc_prime = True
        while len(str_num) > 0:
            if not isprime(int(str_num)):
                is_trunc_prime = False
                break
            str_num = str_num[1:]
        if is_trunc_prime:
            primes.append(num)
    return sorted(primes)
