
def all_right_truncatable_prime(nums):
    primes = []
    for num in nums:
        if is_right_truncatable_prime(num):
            primes.append(num)
    return sorted(primes, reverse=True)
