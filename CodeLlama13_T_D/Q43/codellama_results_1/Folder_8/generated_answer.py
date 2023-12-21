
def find_primes_between_indices(nums):
    primes = []
    for i in range(43, 76 + 1):
        if is_prime(nums[i]):
            primes.append(nums[i])
    return sorted(primes, reverse=True)
