
from sympy import isprime

def all_left_right_truncatable_prime(nums):
    x = nums[618]
    truncated_primes = []
    for num in range(22, x + 1):
        if num % 10 in {0, 2, 4, 5, 6, 8} or num % 10 == 0 or '0' in str(num):
            continue
        if all(isprime(int(str(num)[:i])) and isprime(int(str(num)[i:])) for i in range(1, len(str(num)))):
            truncated_primes.append(num)
    return sorted(truncated_primes)
