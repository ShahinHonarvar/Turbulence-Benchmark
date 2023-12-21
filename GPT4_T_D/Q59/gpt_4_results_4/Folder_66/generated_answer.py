
from sympy import isprime

def all_left_truncatable_prime(nums):
    x = nums[25]
    left_truncatable_primes = []

    for number in range(2, x):
        if number != 0 and isprime(number):
            number_str = str(number)
            if all(isprime(int(number_str[n:])) for n in range(len(number_str))):
                left_truncatable_primes.append(number)

    return sorted(left_truncatable_primes, reverse=True)
