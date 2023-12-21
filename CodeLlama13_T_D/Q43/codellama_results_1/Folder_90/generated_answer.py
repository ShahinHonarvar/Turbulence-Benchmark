
def find_primes_between_indices(nums):
    primes = []
    for i in range(413, 449):
        if nums[i] not in primes and is_prime(nums[i]):
            primes.append(nums[i])
    return sorted(primes)
