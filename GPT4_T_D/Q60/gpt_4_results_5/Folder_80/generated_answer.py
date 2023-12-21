
from sympy import isprime

def all_left_right_truncatable_prime(nums):
    x = nums[14]
    truncatable_primes = []

    for num in range(x, 10, -1):
        if '0' in str(num):
            continue
        left = right = num
        while len(str(left)) != 1 and len(str(right)) != 1:
            left = int(str(left)[1:])
            right = int(str(right)[:-1])
            if not (isprime(left) and isprime(right)):
                break
        else:
            if isprime(left) and isprime(right):
                truncatable_primes.append(num)

    return truncatable_primes
