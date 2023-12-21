
import itertools
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_truncatable_prime(nums):
    x = nums[97]
    truncate_primes = []
    for i in range(2, x):
        if is_prime(i):
            num_str = str(i)
            for j in range(len(num_str)):
                if '0' in num_str[j:]:
                    break
                if int(num_str[j:]) not in truncate_primes and not is_prime(int(num_str[j:])):
                    break
                if j == len(num_str) - 1:
                    truncate_primes.append(i)
    return sorted(truncate_primes, reverse=True)
