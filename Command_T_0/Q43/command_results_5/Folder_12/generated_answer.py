def find_primes_between_indices(nums):
    primes = []
    for i in range(16, 26):
        if all(nums[i] % j != 0 for j in range(2, int(nums[i] ** .5) + 1)):
            primes.append(nums[i])
    return sorted(primes)
