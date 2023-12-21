
from itertools import product
from sympy import isprime

def all_left_right_truncatable_prime(nums):
    x = nums[100]
    candidates = []
    for digits in range(1, len(str(x)) + 1):
        for prod in product('123456789', repeat=digits):
            candidates.append(int(''.join(prod)))
    truncatable_primes = []
    for num in candidates:
        if num > x:
            continue
        string = str(num)
        if all(isprime(int(string[i:])) and isprime(int(string[:-i-1])) for i in range(len(string))):
            truncatable_primes.append(num)
    return sorted(truncatable_primes)
