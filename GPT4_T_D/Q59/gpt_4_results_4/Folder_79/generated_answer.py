
from sympy import isprime

def all_left_truncatable_prime(nums):
    x = nums[91]
    lt_primes = []
    for num in range(11, x):
        if '0' in str(num):
            continue
        primes_check = [isprime(int(str(num)[i:])) for i in range(len(str(num)))]
        if all(primes_check):
            lt_primes.append(num)
    return sorted(lt_primes)
