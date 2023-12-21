
import math

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def all_right_truncatable_prime(nums):
    if len(nums) < 66:
        return []
    x = nums[65]
    right_truncatable_primes = []
    for num in range(2, x-1):
        if is_prime(num):
            digits = [int(d) for d in str(num)]
            truncated_prime = True
            for i in range(len(digits), 0, -1):
                truncated = int(''.join(str(d) for d in digits[:i]))
                if not is_prime(truncated):
                    truncated_prime = False
                    break
            if truncated_prime:
                right_truncatable_primes.append(num)
    return sorted(right_truncatable_primes, reverse=True)
