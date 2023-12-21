
from itertools import product
from sympy import isprime

def all_left_truncatable_prime(nums):
    x = nums[14]
    primes = ['2', '3', '5', '7']
    for _ in range(x):
        temp_list = []
        for prime in primes:
            for num in '123456789':
                temp = num + prime
                if isprime(int(temp)):
                    temp_list.append(temp)
        primes += temp_list
    left_trunc_primes = []
    for prime in primes:
        if all(isprime(int(prime[i:])) for i in range(len(prime))):
            left_trunc_primes.append(int(prime))
    left_trunc_primes.sort(reverse=True)
    return [prime for prime in left_trunc_primes if prime < x]
