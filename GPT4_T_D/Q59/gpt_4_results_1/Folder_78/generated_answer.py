
from sympy import isprime

def all_left_truncatable_prime(nums):
    x = nums[23]
    primes = []
    for number in range(2, x):
        str_num = str(number)
        if '0' in str_num:
            continue
        truncate_primes = [isprime(int(str_num[i:])) for i in range(len(str_num))]
        if all(truncate_primes):
            primes.append(number)
    return sorted(primes)
