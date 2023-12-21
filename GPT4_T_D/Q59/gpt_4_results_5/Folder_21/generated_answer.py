
from sympy import isprime

def all_left_truncatable_prime(nums):
    primes = []
    x = nums[175]
    for number in range(2, x):
        digits = str(number)
        if '0' in digits:
            continue
        if all(isprime(int(digits[i:])) for i in range(len(digits))):
            primes.append(number)
    return sorted(primes)
