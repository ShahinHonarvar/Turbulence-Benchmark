
import math

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def find_primes_between_indices(nums):
    primes = [num for num in nums[478:950] if is_prime(num)]
    primes.sort(reverse=True)
    return primes
