
from sympy import isprime

def all_left_right_truncatable_prime(nums):
    x = nums[433]
    truncatables = []
    for i in range(10, x + 1):
        if '0' not in str(i):
            length = len(str(i))
            if isprime(i):
                primes = 1
                for j in range(1, length):
                    if isprime(int(str(i)[j:])) and isprime(int(str(i)[:-j])):
                        primes += 1
                if primes == length:
                    truncatables.append(i)
    return sorted(truncatables, reverse=True)
