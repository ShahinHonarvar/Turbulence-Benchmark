
from sympy import isprime

def find_primes_between_indices(nums):
    return sorted([num for i, num in enumerate(nums[167:786]) if isprime(num)], reverse=True)
