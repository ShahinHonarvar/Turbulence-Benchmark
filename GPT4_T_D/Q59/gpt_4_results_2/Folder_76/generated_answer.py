
from sympy import isprime

def all_left_truncatable_prime(nums):
    x = nums[370]
    primes = []
    for num in range(2, x):
        num_str = str(num)
        if '0' in num_str:
            continue
        is_left_truncatable_prime = True
        while len(num_str) > 0 and is_left_truncatable_prime:
            if not isprime(int(num_str)):
                is_left_truncatable_prime = False
            num_str = num_str[1:]
        if is_left_truncatable_prime:
            primes.append(num)
    primes.sort(reverse=True)
    return primes
