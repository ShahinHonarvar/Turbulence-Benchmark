
def all_left_truncatable_prime(nums):
    x = nums[64]
    left_truncatable_primes = []
    for i in range(x):
        if is_prime(i) and not '0' in str(i):
            left_truncatable_primes.append(i)
    return sorted(left_truncatable_primes, reverse=True)
