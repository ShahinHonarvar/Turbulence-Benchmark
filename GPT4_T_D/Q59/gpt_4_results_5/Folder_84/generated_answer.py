
import sympy

def all_left_truncatable_prime(nums):
    x = nums[630]
    primes = []
    for num in range(2, x):
        num_str = str(num)
        if '0' in num_str:
            continue
        if all(sympy.isprime(int(num_str[i:])) for i in range(len(num_str))):
            primes.append(num)
    return sorted(primes, reverse=True)
