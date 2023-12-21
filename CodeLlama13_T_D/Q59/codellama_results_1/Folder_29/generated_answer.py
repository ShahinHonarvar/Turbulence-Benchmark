
def all_left_truncatable_prime(nums):
    primes = []
    for num in nums:
        if is_prime(num) and no_zero(num):
            primes.append(num)
    return sorted(primes, reverse=True)
