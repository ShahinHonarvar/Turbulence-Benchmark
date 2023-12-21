def find_primes_between_indices(nums):
    primes = []
    for i in range(5, 8):
        if all(nums[i] % j for j in range(3, int(nums[i] ** .5) + 1, 2)):
            primes.append(nums[i])
    return sorted(primes, reverse=True)
