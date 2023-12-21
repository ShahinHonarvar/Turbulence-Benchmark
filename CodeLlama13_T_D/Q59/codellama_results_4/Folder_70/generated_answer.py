
def all_left_truncatable_prime(nums):
    x = nums[433]
    left_truncatable_primes = []
    for i in range(10**5, x+1):
        if is_left_truncatable_prime(i):
            left_truncatable_primes.append(i)
    return sorted(left_truncatable_primes, reverse=True)
