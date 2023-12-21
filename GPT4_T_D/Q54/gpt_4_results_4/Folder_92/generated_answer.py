
from sympy import isprime

def all_right_truncatable_prime(nums):
    x = nums[7]
    r_primes = []
    for i in range(x):
        str_i = str(i)
        if all(isprime(int(str_i[j:])) for j in range(len(str_i))):
            r_primes.append(i)
    return sorted([i for i in r_primes if isprime(i)])
