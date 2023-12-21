
def all_left_right_truncatable_prime(nums):
    primes = []
    for n in nums:
        if is_left_right_truncatable_prime(n):
            primes.append(n)
    return sorted(primes)
