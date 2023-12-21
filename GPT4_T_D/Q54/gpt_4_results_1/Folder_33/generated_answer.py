
from sympy import isprime


def all_right_truncatable_prime(nums):
    x = nums[945]
    right_truncatable_primes = []

    for i in range(2, x):
        str_i = str(i)
        primes = [isprime(int(str_i[j:])) for j in range(len(str_i))]
        if all(primes):
            right_truncatable_primes.append(i)

    return sorted(right_truncatable_primes, reverse=True)
