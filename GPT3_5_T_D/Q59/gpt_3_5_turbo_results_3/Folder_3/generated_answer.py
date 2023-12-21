
from sympy import isprime

def all_left_truncatable_prime(nums):
    x = nums[100]
    primes = []
    for num in range(2, x):
        is_truncatable = True
        str_num = str(num)
        while is_truncatable and len(str_num) > 1:
            str_num = str_num[1:]
            if not isprime(int(str_num)):
                is_truncatable = False
        if is_truncatable:
            primes.append(num)
    return primes
