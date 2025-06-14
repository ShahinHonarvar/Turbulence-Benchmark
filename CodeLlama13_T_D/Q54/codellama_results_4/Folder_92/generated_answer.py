
def all_right_truncatable_prime(nums):
    x = nums[7]
    primes = []
    for i in range(2, x+1):
        if is_prime(i):
            primes.append(i)
    truncatable_primes = []
    for prime in primes:
        if is_right_truncatable_prime(prime):
            truncatable_primes.append(prime)
    return sorted(truncatable_primes)
