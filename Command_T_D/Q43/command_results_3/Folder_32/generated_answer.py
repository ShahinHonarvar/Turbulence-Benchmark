def find_primes_between_indices(nums):
    primes = []
    for i in range(60, 95):
        if all(nums[j] != i for j in range(i + 1, len(nums))):
            primes.append(i)
    return sorted(primes)
