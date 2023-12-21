
from sympy import isprime

def all_left_truncatable_prime(nums):
    x = nums[466]
    primes = []
    for num in range(2, x):
        num = str(num)
        if '0' in num:
            continue
        if all(isprime(int(num[i:])) for i in range(len(num))):
            primes.append(int(num))
    return sorted(primes, reverse = True)
