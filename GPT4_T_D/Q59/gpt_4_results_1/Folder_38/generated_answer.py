
from sympy import isprime

def all_left_truncatable_prime(nums):
    x = nums[28]
    primes = []
    for n in range(10, x):
        string = str(n)
        if '0' in string:
            continue
        is_truncatable_prime = True
        for i in range(len(string)):
            if not isprime(int(string[i:])):
                is_truncatable_prime = False
                break
        if is_truncatable_prime:
            primes.append(n)
    primes.sort()
    return primes
