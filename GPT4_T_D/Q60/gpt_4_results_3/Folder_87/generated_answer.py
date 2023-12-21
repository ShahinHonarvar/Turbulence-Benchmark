
from sympy import isprime

def all_left_right_truncatable_prime(nums):
    x = nums[39]
    primes = []
    for num in range(2, x + 1):
        num_str = str(num)
        if '0' in num_str:
            continue
        i = 1
        while True:
            if not isprime(int(num_str[i:])) or not isprime(int(num_str[:i])):
                break
            i += 1 
            if i == len(num_str):
                primes.append(num)
                break
    return sorted(primes, reverse=True)
