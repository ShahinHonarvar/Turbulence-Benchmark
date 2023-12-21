
from sympy import isprime

def all_left_truncatable_prime(nums):
    x = nums[50]
    truncatable_primes = []
    for number in range(x):
        if number > 1 and all(isprime(int(str(number)[:i])) for i in range(1, len(str(number))+1)) and '0' not in str(number):
            truncatable_primes.append(number)
    return sorted(truncatable_primes, reverse=True)
