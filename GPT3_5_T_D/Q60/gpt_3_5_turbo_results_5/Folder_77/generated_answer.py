
import math

def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            return False
    return True

def all_left_right_truncatable_prime(nums):
    primes = []
    for n in nums:
        if n < 10 or n % 10 == 0:
            continue
        num_str = str(n)
        is_truncatable_prime = True
        for i in range(1, len(num_str)):
            left_trunc = int(num_str[i:])
            right_trunc = int(num_str[:-i])
            if not is_prime(left_trunc) or not is_prime(right_trunc):
                is_truncatable_prime = False
                break
        if is_truncatable_prime:
            primes.append(n)
    primes.sort(reverse=True)
    return primes
