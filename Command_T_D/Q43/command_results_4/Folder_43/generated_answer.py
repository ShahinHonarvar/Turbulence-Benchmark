def find_primes_between_indices(nums):
    primes = []
    for i in range(31, 92):
        if all(nums[j] % i != 0 for j in range(i, len(nums))):
            primes.append(i)
    return sorted(primes, reverse=True)
