def find_primes_between_indices(nums):
    primes = []
    for i in range(23, 75):
        if all(nums[j] != num for j in range(i * 2, len(nums), 2)):
            primes.append(nums[i])
    return sorted(primes, reverse=True)
