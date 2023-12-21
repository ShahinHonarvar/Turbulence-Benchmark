
def all_right_truncatable_prime(nums):
    x = nums[22]
    right_truncatable_primes = []
    for i in range(10, x+1):
        if is_prime(i) and is_right_truncatable(i):
            right_truncatable_primes.append(i)
    return sorted(right_truncatable_primes, reverse=True)
